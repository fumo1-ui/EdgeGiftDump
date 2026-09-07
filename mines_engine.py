import datetime
import math
import random
import uuid

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    return math.comb(n, r)

def calc_multiplier(bombs, opened):
    if opened == 0:
        return 1.0
    total = 25
    safe = total - bombs
    prob = nCr(safe, opened) / nCr(total, opened)
    mult = (1.0 / prob) * 0.96
    return max(1.01, round(mult * 100) / 100)

class MinesEngine:
    def __init__(self, get_user_balance, update_user_balance):
        self.get_user_balance = get_user_balance
        self.update_user_balance = update_user_balance
        self.session = None

    def get_state(self):
        if not self.session:
            return {"ok": True, "state": None}
        return {"ok": True, "state": self._public_session()}

    def get_limits(self, bombs_req=3):
        bombs_applied = max(1, min(24, int(bombs_req)))
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        return {
            "ok": True,
            "quoteId": f"quote-{uuid.uuid4()}",
            "quoteExpiresAt": "2030-01-01T00:00:00.000Z",
            "serverTime": now,
            "allowed": {
                "maxBetAllowed": 50000,
                "maxPayout": 10000000,
                "maxMultiplierX100": 10000000
            },
            "bombs": {
                "requested": int(bombs_req),
                "applied": bombs_applied,
                "minForX1": 1,
                "range": {"min": 1, "max": 24}
            }
        }

    def start_game(self, data):
        bet = int(data.get("bet", 100))
        currency = data.get("currency", "gold")
        bombs = max(1, min(24, int(data.get("bombs", 3))))
        size = int(data.get("size", 5))

        gold, silver = self.get_user_balance()
        if currency == "gold" and gold < bet:
            return {"ok": False, "errorCode": "INSUFFICIENT_FUNDS"}
        if currency == "silver" and silver < bet:
            return {"ok": False, "errorCode": "INSUFFICIENT_FUNDS"}

        # Deduct bet
        if currency == "gold":
            self.update_user_balance(gold - bet, silver)
        else:
            self.update_user_balance(gold, silver - bet)

        gold, silver = self.get_user_balance()

        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        expires = (datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2)).isoformat()

        bomb_positions = sorted(random.sample(range(25), bombs))
        mult_table = [int(calc_multiplier(bombs, k) * 100) for k in range(1, 25 - bombs + 1)]
        next_mult = calc_multiplier(bombs, 1)

        self.session = {
            "sessionId": f"mines-{uuid.uuid4()}",
            "status": "active",
            "currency": currency,
            "size": size,
            "bombs": bombs,
            "bet": bet,
            "startedAt": now,
            "lastActionAt": now,
            "expiresAt": expires,
            "betChargedAt": now,
            "openedCells": [],
            "openedCount": 0,
            "safeTotal": 25 - bombs,
            "remainingSafe": 25 - bombs,
            "lastReveal": None,
            "cashoutMultiplierX100": 100,
            "cashoutPayoutTotal": bet,
            "coinsRemainder": 0,
            "reserved": 0,
            "nextMultiplierX100": int(next_mult * 100),
            "nextPayoutTotal": int(bet * next_mult),
            "nextRevealAllowed": True,
            "nextBlockedReason": None,
            "multiplierTableX100": mult_table,
            "limits": {
                "maxPayout": 10000000,
                "maxMultiplierX100": 10000000,
                "configVersion": 1
            },
            "balance": {"gold": gold, "silver": silver},
            "_bombPositions": bomb_positions
        }
        return {"ok": True, "state": self._public_session()}

    def reveal_cell(self, cell_index):
        if not self.session or self.session["status"] != "active":
            return {"ok": False, "errorCode": "NO_ACTIVE_SESSION"}

        if cell_index in self.session["openedCells"]:
            return {"ok": True, "state": self._public_session()}

        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        self.session["lastActionAt"] = now

        if cell_index in self.session["_bombPositions"]:
            self.session["status"] = "lost"
            self.session["lastReveal"] = {"cellIndex": cell_index, "isBomb": True}
            self.session["bombPositions"] = self.session["_bombPositions"]
            self.session["nextRevealAllowed"] = False
            self.session["nextMultiplierX100"] = None
            self.session["nextPayoutTotal"] = None
            return {"ok": True, "state": self._public_session()}

        self.session["openedCells"].append(cell_index)
        self.session["openedCount"] += 1
        self.session["remainingSafe"] -= 1

        mult = calc_multiplier(self.session["bombs"], self.session["openedCount"])
        self.session["cashoutMultiplierX100"] = int(mult * 100)
        self.session["cashoutPayoutTotal"] = int(self.session["bet"] * mult)
        self.session["lastReveal"] = {"cellIndex": cell_index, "isBomb": False}

        if self.session["remainingSafe"] == 0:
            self.session["status"] = "cashed_out"
            self.session["bombPositions"] = self.session["_bombPositions"]
            self.session["nextRevealAllowed"] = False
            self.session["nextMultiplierX100"] = None
            self.session["nextPayoutTotal"] = None
            gold, silver = self.get_user_balance()
            payout = self.session["cashoutPayoutTotal"]
            if self.session["currency"] == "gold":
                self.update_user_balance(gold + payout, silver)
            else:
                self.update_user_balance(gold, silver + payout)
        else:
            next_mult = calc_multiplier(self.session["bombs"], self.session["openedCount"] + 1)
            self.session["nextMultiplierX100"] = int(next_mult * 100)
            self.session["nextPayoutTotal"] = int(self.session["bet"] * next_mult)

        gold, silver = self.get_user_balance()
        self.session["balance"] = {"gold": gold, "silver": silver}
        return {"ok": True, "state": self._public_session()}

    def cashout(self):
        if not self.session or self.session["status"] != "active":
            return {"ok": False, "errorCode": "NO_ACTIVE_SESSION"}

        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        self.session["lastActionAt"] = now
        self.session["status"] = "cashed_out"
        self.session["bombPositions"] = self.session["_bombPositions"]
        self.session["nextRevealAllowed"] = False
        self.session["nextMultiplierX100"] = None
        self.session["nextPayoutTotal"] = None

        gold, silver = self.get_user_balance()
        payout = self.session["cashoutPayoutTotal"]
        if self.session["currency"] == "gold":
            self.update_user_balance(gold + payout, silver)
        else:
            self.update_user_balance(gold, silver + payout)

        gold, silver = self.get_user_balance()
        self.session["balance"] = {"gold": gold, "silver": silver}
        return {"ok": True, "state": self._public_session()}

    def _public_session(self):
        return {k: v for k, v in self.session.items() if not k.startswith("_")}
