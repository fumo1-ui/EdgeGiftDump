import http.server
import socketserver
import json
import urllib.parse
import os
import sys
import datetime

PORT = 8080
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

ALL_GIFTS = [
  {
    "itemKey": "gift-5168043875654172773",
    "telegramGiftId": "5168043875654172773",
    "giftName": "Cup",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5168043875654172773",
      "previewUrl": "https://edge.gift/gift-assets/5168043875654172773/fixed-511716a675d8c748/preview.png?v=fixed-511716a675d8c748",
      "animationUrl": "https://edge.gift/gift-assets/5168043875654172773/fixed-511716a675d8c748/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5168103777563050263",
    "telegramGiftId": "5168103777563050263",
    "giftName": "Rose",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5168103777563050263",
      "previewUrl": "https://edge.gift/gift-assets/5168103777563050263/fixed-4928911cdafc934a/preview.png?v=fixed-4928911cdafc934a",
      "animationUrl": "https://edge.gift/gift-assets/5168103777563050263/fixed-4928911cdafc934a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170144170496491616",
    "telegramGiftId": "5170144170496491616",
    "giftName": "Cake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170144170496491616",
      "previewUrl": "https://edge.gift/gift-assets/5170144170496491616/fixed-69d87ea82c08d957/preview.png?v=fixed-69d87ea82c08d957",
      "animationUrl": "https://edge.gift/gift-assets/5170144170496491616/fixed-69d87ea82c08d957/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170145012310081615",
    "telegramGiftId": "5170145012310081615",
    "giftName": "Heart",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170145012310081615",
      "previewUrl": "https://edge.gift/gift-assets/5170145012310081615/fixed-fe56df461e6287b0/preview.png?v=fixed-fe56df461e6287b0",
      "animationUrl": "https://edge.gift/gift-assets/5170145012310081615/fixed-fe56df461e6287b0/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170233102089322756",
    "telegramGiftId": "5170233102089322756",
    "giftName": "Bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170233102089322756",
      "previewUrl": "https://edge.gift/gift-assets/5170233102089322756/fixed-eaebe8b60e286533/preview.png?v=fixed-eaebe8b60e286533",
      "animationUrl": "https://edge.gift/gift-assets/5170233102089322756/fixed-eaebe8b60e286533/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170250947678437525",
    "telegramGiftId": "5170250947678437525",
    "giftName": "Box",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170250947678437525",
      "previewUrl": "https://edge.gift/gift-assets/5170250947678437525/fixed-e5f065b352ea5b5b/preview.png?v=fixed-e5f065b352ea5b5b",
      "animationUrl": "https://edge.gift/gift-assets/5170250947678437525/fixed-e5f065b352ea5b5b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170314324215857265",
    "telegramGiftId": "5170314324215857265",
    "giftName": "Flowers",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170314324215857265",
      "previewUrl": "https://edge.gift/gift-assets/5170314324215857265/fixed-46cf04eea2d6d508/preview.png?v=fixed-46cf04eea2d6d508",
      "animationUrl": "https://edge.gift/gift-assets/5170314324215857265/fixed-46cf04eea2d6d508/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170521118301225164",
    "telegramGiftId": "5170521118301225164",
    "giftName": "Crystal",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170521118301225164",
      "previewUrl": "https://edge.gift/gift-assets/5170521118301225164/fixed-7a24ef9dff524778/preview.png?v=fixed-7a24ef9dff524778",
      "animationUrl": "https://edge.gift/gift-assets/5170521118301225164/fixed-7a24ef9dff524778/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170564780938756245",
    "telegramGiftId": "5170564780938756245",
    "giftName": "Rocket",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170564780938756245",
      "previewUrl": "https://edge.gift/gift-assets/5170564780938756245/fixed-647cd586497cd982/preview.png?v=fixed-647cd586497cd982",
      "animationUrl": "https://edge.gift/gift-assets/5170564780938756245/fixed-647cd586497cd982/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5170690322832818290",
    "telegramGiftId": "5170690322832818290",
    "giftName": "Ring",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5170690322832818290",
      "previewUrl": "https://edge.gift/gift-assets/5170690322832818290/fixed-ee8dc00f07e57fa1/preview.png?v=fixed-ee8dc00f07e57fa1",
      "animationUrl": "https://edge.gift/gift-assets/5170690322832818290/fixed-ee8dc00f07e57fa1/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5800655655995968830",
    "telegramGiftId": "5800655655995968830",
    "giftName": "5800655655995968830",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5800655655995968830",
      "previewUrl": "https://edge.gift/gift-assets/5800655655995968830/fixed-9b243920ad395aa3/preview.png?v=fixed-9b243920ad395aa3",
      "animationUrl": "https://edge.gift/gift-assets/5800655655995968830/fixed-9b243920ad395aa3/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5801108895304779062",
    "telegramGiftId": "5801108895304779062",
    "giftName": "5801108895304779062",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5801108895304779062",
      "previewUrl": "https://edge.gift/gift-assets/5801108895304779062/fixed-4267c007f982dbce/preview.png?v=fixed-4267c007f982dbce",
      "animationUrl": "https://edge.gift/gift-assets/5801108895304779062/fixed-4267c007f982dbce/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5866352046986232958",
    "telegramGiftId": "5866352046986232958",
    "giftName": "5866352046986232958",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5866352046986232958",
      "previewUrl": "https://edge.gift/gift-assets/5866352046986232958/fixed-5ae3bdd851db57c8/preview.png?v=fixed-5ae3bdd851db57c8",
      "animationUrl": "https://edge.gift/gift-assets/5866352046986232958/fixed-5ae3bdd851db57c8/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5893356958802511476",
    "telegramGiftId": "5893356958802511476",
    "giftName": "5893356958802511476",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5893356958802511476",
      "previewUrl": "https://edge.gift/gift-assets/5893356958802511476/fixed-307b9b48a0ad6df4/preview.png?v=fixed-307b9b48a0ad6df4",
      "animationUrl": "https://edge.gift/gift-assets/5893356958802511476/fixed-307b9b48a0ad6df4/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5922558454332916696",
    "telegramGiftId": "5922558454332916696",
    "giftName": "5922558454332916696",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5922558454332916696",
      "previewUrl": "https://edge.gift/gift-assets/5922558454332916696/fixed-2a023fcdb24b6ee2/preview.png?v=fixed-2a023fcdb24b6ee2",
      "animationUrl": "https://edge.gift/gift-assets/5922558454332916696/fixed-2a023fcdb24b6ee2/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5956217000635139069",
    "telegramGiftId": "5956217000635139069",
    "giftName": "5956217000635139069",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5956217000635139069",
      "previewUrl": "https://edge.gift/gift-assets/5956217000635139069/fixed-d68b6acbff2c8cbd/preview.png?v=fixed-d68b6acbff2c8cbd",
      "animationUrl": "https://edge.gift/gift-assets/5956217000635139069/fixed-d68b6acbff2c8cbd/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5969796561943660080",
    "telegramGiftId": "5969796561943660080",
    "giftName": "Bunny Bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5969796561943660080",
      "previewUrl": "https://edge.gift/gift-assets/5969796561943660080/fixed-9ea09c6b271187bb/preview.png?v=fixed-9ea09c6b271187bb",
      "animationUrl": "https://edge.gift/gift-assets/5969796561943660080/fixed-9ea09c6b271187bb/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-5974210632977745012",
    "telegramGiftId": "5974210632977745012",
    "giftName": "Soccer Bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "5974210632977745012",
      "previewUrl": "https://edge.gift/gift-assets/5974210632977745012/fixed-16041defa1a46095/preview.png?v=fixed-16041defa1a46095",
      "animationUrl": "https://edge.gift/gift-assets/5974210632977745012/fixed-16041defa1a46095/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-6026193266406327981",
    "telegramGiftId": "6026193266406327981",
    "giftName": "Worker Bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "6026193266406327981",
      "previewUrl": "https://edge.gift/gift-assets/6026193266406327981/fixed-728ade9b8326ef23/preview.png?v=fixed-728ade9b8326ef23",
      "animationUrl": "https://edge.gift/gift-assets/6026193266406327981/fixed-728ade9b8326ef23/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-6028601630662853006",
    "telegramGiftId": "6028601630662853006",
    "giftName": "Bottle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "6028601630662853006",
      "previewUrl": "https://edge.gift/gift-assets/6028601630662853006/fixed-672295baeaa64fbf/preview.png?v=fixed-672295baeaa64fbf",
      "animationUrl": "https://edge.gift/gift-assets/6028601630662853006/fixed-672295baeaa64fbf/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-6046178578163303744",
    "telegramGiftId": "6046178578163303744",
    "giftName": "911 Bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "6046178578163303744",
      "previewUrl": "https://edge.gift/gift-assets/6046178578163303744/fixed-c85efee4f6fa2ebb/preview.png?v=fixed-c85efee4f6fa2ebb",
      "animationUrl": "https://edge.gift/gift-assets/6046178578163303744/fixed-c85efee4f6fa2ebb/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgAD2G8AAqr9OEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgAD2G8AAqr9OEs",
    "giftName": "NewGiftsByAutoGiftNews_AgAD2G8AAqr9OEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgAD2G8AAqr9OEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD2G8AAqr9OEs/sha256-bc933b481faa626d/preview.webp?v=sha256-bc933b481faa626d",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD2G8AAqr9OEs/sha256-bc933b481faa626d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgAD2HQAAp5oiEg",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgAD2HQAAp5oiEg",
    "giftName": "NewGiftsByAutoGiftNews_AgAD2HQAAp5oiEg",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgAD2HQAAp5oiEg",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD2HQAAp5oiEg/sha256-4a53dc69a7f94bc7/preview.webp?v=sha256-4a53dc69a7f94bc7",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD2HQAAp5oiEg/sha256-4a53dc69a7f94bc7/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgAD4nEAAgQpOUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgAD4nEAAgQpOUs",
    "giftName": "NewGiftsByAutoGiftNews_AgAD4nEAAgQpOUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgAD4nEAAgQpOUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD4nEAAgQpOUs/sha256-39b331a6fe9b237e/preview.webp?v=sha256-39b331a6fe9b237e",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD4nEAAgQpOUs/sha256-39b331a6fe9b237e/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgAD6X0AAiIeUUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgAD6X0AAiIeUUs",
    "giftName": "NewGiftsByAutoGiftNews_AgAD6X0AAiIeUUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgAD6X0AAiIeUUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD6X0AAiIeUUs/sha256-4f546ce6d20f50d9/preview.webp?v=sha256-4f546ce6d20f50d9",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD6X0AAiIeUUs/sha256-4f546ce6d20f50d9/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgAD7GUAAgSmOEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgAD7GUAAgSmOEs",
    "giftName": "NewGiftsByAutoGiftNews_AgAD7GUAAgSmOEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgAD7GUAAgSmOEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD7GUAAgSmOEs/sha256-7854c9ca9300a36a/preview.webp?v=sha256-7854c9ca9300a36a",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD7GUAAgSmOEs/sha256-7854c9ca9300a36a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgAD9WkAArpjOUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgAD9WkAArpjOUs",
    "giftName": "NewGiftsByAutoGiftNews_AgAD9WkAArpjOUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgAD9WkAArpjOUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD9WkAArpjOUs/sha256-c57ee766ac7ec68a/preview.webp?v=sha256-c57ee766ac7ec68a",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgAD9WkAArpjOUs/sha256-c57ee766ac7ec68a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADDW0AAsHmMEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADDW0AAsHmMEs",
    "giftName": "NewGiftsByAutoGiftNews_AgADDW0AAsHmMEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADDW0AAsHmMEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADDW0AAsHmMEs/sha256-1c43c1f124172325/preview.webp?v=sha256-1c43c1f124172325",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADDW0AAsHmMEs/sha256-1c43c1f124172325/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADDW8AAoqZSUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADDW8AAoqZSUs",
    "giftName": "NewGiftsByAutoGiftNews_AgADDW8AAoqZSUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADDW8AAoqZSUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADDW8AAoqZSUs/sha256-9716b555879789ce/preview.webp?v=sha256-9716b555879789ce",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADDW8AAoqZSUs/sha256-9716b555879789ce/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADEGoAAgSUMEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADEGoAAgSUMEs",
    "giftName": "NewGiftsByAutoGiftNews_AgADEGoAAgSUMEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADEGoAAgSUMEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADEGoAAgSUMEs/sha256-388f624630335408/preview.webp?v=sha256-388f624630335408",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADEGoAAgSUMEs/sha256-388f624630335408/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADKHgAAhFA6Eg",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADKHgAAhFA6Eg",
    "giftName": "NewGiftsByAutoGiftNews_AgADKHgAAhFA6Eg",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADKHgAAhFA6Eg",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADKHgAAhFA6Eg/sha256-1881e7bbe96b0b81/preview.webp?v=sha256-1881e7bbe96b0b81",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADKHgAAhFA6Eg/sha256-1881e7bbe96b0b81/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADKnoAArubIUg",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADKnoAArubIUg",
    "giftName": "NewGiftsByAutoGiftNews_AgADKnoAArubIUg",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADKnoAArubIUg",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADKnoAArubIUg/sha256-1fef958ae28bfcd9/preview.webp?v=sha256-1fef958ae28bfcd9",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADKnoAArubIUg/sha256-1fef958ae28bfcd9/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADLXUAAhUOQUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADLXUAAhUOQUs",
    "giftName": "NewGiftsByAutoGiftNews_AgADLXUAAhUOQUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADLXUAAhUOQUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADLXUAAhUOQUs/sha256-efa6fc5dcd35e671/preview.webp?v=sha256-efa6fc5dcd35e671",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADLXUAAhUOQUs/sha256-efa6fc5dcd35e671/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADO20AAic2MEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADO20AAic2MEs",
    "giftName": "NewGiftsByAutoGiftNews_AgADO20AAic2MEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADO20AAic2MEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADO20AAic2MEs/sha256-c47da93ed324ac5e/preview.webp?v=sha256-c47da93ed324ac5e",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADO20AAic2MEs/sha256-c47da93ed324ac5e/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADS4IAApQf2Uk",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADS4IAApQf2Uk",
    "giftName": "NewGiftsByAutoGiftNews_AgADS4IAApQf2Uk",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADS4IAApQf2Uk",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADS4IAApQf2Uk/sha256-6e480a74bab655fb/preview.webp?v=sha256-6e480a74bab655fb",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADS4IAApQf2Uk/sha256-6e480a74bab655fb/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADTWQAAmVlMUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADTWQAAmVlMUs",
    "giftName": "NewGiftsByAutoGiftNews_AgADTWQAAmVlMUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADTWQAAmVlMUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADTWQAAmVlMUs/sha256-cefc0a4e738bb02d/preview.webp?v=sha256-cefc0a4e738bb02d",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADTWQAAmVlMUs/sha256-cefc0a4e738bb02d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADYXkAAvFiWEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADYXkAAvFiWEs",
    "giftName": "NewGiftsByAutoGiftNews_AgADYXkAAvFiWEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADYXkAAvFiWEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADYXkAAvFiWEs/sha256-1fe5f36bc745bb45/preview.webp?v=sha256-1fe5f36bc745bb45",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADYXkAAvFiWEs/sha256-1fe5f36bc745bb45/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADcXEAAjVZWUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADcXEAAjVZWUs",
    "giftName": "NewGiftsByAutoGiftNews_AgADcXEAAjVZWUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADcXEAAjVZWUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADcXEAAjVZWUs/sha256-ada203ce999673f8/preview.webp?v=sha256-ada203ce999673f8",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADcXEAAjVZWUs/sha256-ada203ce999673f8/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADdYAAAt_J2Uk",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADdYAAAt_J2Uk",
    "giftName": "NewGiftsByAutoGiftNews_AgADdYAAAt_J2Uk",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADdYAAAt_J2Uk",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADdYAAAt_J2Uk/sha256-02dba1018e3f98e2/preview.webp?v=sha256-02dba1018e3f98e2",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADdYAAAt_J2Uk/sha256-02dba1018e3f98e2/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADdYcAAk9R6Ug",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADdYcAAk9R6Ug",
    "giftName": "NewGiftsByAutoGiftNews_AgADdYcAAk9R6Ug",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADdYcAAk9R6Ug",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADdYcAAk9R6Ug/sha256-4c8471c97e5084b8/preview.webp?v=sha256-4c8471c97e5084b8",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADdYcAAk9R6Ug/sha256-4c8471c97e5084b8/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADdmoAAscGMUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADdmoAAscGMUs",
    "giftName": "NewGiftsByAutoGiftNews_AgADdmoAAscGMUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADdmoAAscGMUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADdmoAAscGMUs/sha256-449ca232ca7617cc/preview.webp?v=sha256-449ca232ca7617cc",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADdmoAAscGMUs/sha256-449ca232ca7617cc/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADfmIAAkHQ4Uk",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADfmIAAkHQ4Uk",
    "giftName": "NewGiftsByAutoGiftNews_AgADfmIAAkHQ4Uk",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADfmIAAkHQ4Uk",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADfmIAAkHQ4Uk/sha256-8cd0cdde3fc9708b/preview.webp?v=sha256-8cd0cdde3fc9708b",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADfmIAAkHQ4Uk/sha256-8cd0cdde3fc9708b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADfnkAAtASOEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADfnkAAtASOEs",
    "giftName": "NewGiftsByAutoGiftNews_AgADfnkAAtASOEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADfnkAAtASOEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADfnkAAtASOEs/sha256-b5a33044190e712b/preview.webp?v=sha256-b5a33044190e712b",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADfnkAAtASOEs/sha256-b5a33044190e712b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADh2cAAnngOUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADh2cAAnngOUs",
    "giftName": "NewGiftsByAutoGiftNews_AgADh2cAAnngOUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADh2cAAnngOUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADh2cAAnngOUs/sha256-d2de170ece06ff84/preview.webp?v=sha256-d2de170ece06ff84",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADh2cAAnngOUs/sha256-d2de170ece06ff84/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADi3UAAv-Y6Ug",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADi3UAAv-Y6Ug",
    "giftName": "NewGiftsByAutoGiftNews_AgADi3UAAv-Y6Ug",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADi3UAAv-Y6Ug",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADi3UAAv-Y6Ug/sha256-69cdd9ec70dd8c16/preview.webp?v=sha256-69cdd9ec70dd8c16",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADi3UAAv-Y6Ug/sha256-69cdd9ec70dd8c16/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADiG4AAh1nMUs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADiG4AAh1nMUs",
    "giftName": "NewGiftsByAutoGiftNews_AgADiG4AAh1nMUs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADiG4AAh1nMUs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADiG4AAh1nMUs/sha256-7511912edab95e04/preview.webp?v=sha256-7511912edab95e04",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADiG4AAh1nMUs/sha256-7511912edab95e04/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADl2YAAl0OWEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADl2YAAl0OWEs",
    "giftName": "NewGiftsByAutoGiftNews_AgADl2YAAl0OWEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADl2YAAl0OWEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADl2YAAl0OWEs/sha256-7792ca856f82a4d9/preview.webp?v=sha256-7792ca856f82a4d9",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADl2YAAl0OWEs/sha256-7792ca856f82a4d9/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADymwAAj1GMEs",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADymwAAj1GMEs",
    "giftName": "NewGiftsByAutoGiftNews_AgADymwAAj1GMEs",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADymwAAj1GMEs",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADymwAAj1GMEs/sha256-d43e36c2781c4864/preview.webp?v=sha256-d43e36c2781c4864",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADymwAAj1GMEs/sha256-d43e36c2781c4864/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-NewGiftsByAutoGiftNews_AgADz3YAAhCZwEg",
    "telegramGiftId": "NewGiftsByAutoGiftNews_AgADz3YAAhCZwEg",
    "giftName": "NewGiftsByAutoGiftNews_AgADz3YAAhCZwEg",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "NewGiftsByAutoGiftNews_AgADz3YAAhCZwEg",
      "previewUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADz3YAAhCZwEg/sha256-f1305d81bd8d921d/preview.webp?v=sha256-f1305d81bd8d921d",
      "animationUrl": "https://edge.gift/gift-assets/NewGiftsByAutoGiftNews_AgADz3YAAhCZwEg/sha256-f1305d81bd8d921d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-PremiumStar",
    "telegramGiftId": "PremiumStar",
    "giftName": "PremiumStar",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "PremiumStar",
      "previewUrl": "https://edge.gift/gift-assets/PremiumStar/sha256-bb5994aa406ffc72/preview.webp?v=sha256-bb5994aa406ffc72",
      "animationUrl": "https://edge.gift/gift-assets/PremiumStar/sha256-bb5994aa406ffc72/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-Spinner-Intro",
    "telegramGiftId": "Spinner-Intro",
    "giftName": "Spinner-Intro",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "Spinner-Intro",
      "previewUrl": "https://edge.gift/gift-assets/Spinner-Intro/sha256-e21be43fbfee78f9/preview.webp?v=sha256-e21be43fbfee78f9",
      "animationUrl": "https://edge.gift/gift-assets/Spinner-Intro/sha256-e21be43fbfee78f9/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-artisan_brick",
    "telegramGiftId": "artisan_brick",
    "giftName": "artisan_brick",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "artisan_brick",
      "previewUrl": "https://edge.gift/gift-assets/artisan_brick/sha256-d6b91588102c409b/preview.webp?v=sha256-d6b91588102c409b",
      "animationUrl": "https://edge.gift/gift-assets/artisan_brick/sha256-d6b91588102c409b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-astral_shard",
    "telegramGiftId": "astral_shard",
    "giftName": "astral_shard",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "astral_shard",
      "previewUrl": "https://edge.gift/gift-assets/astral_shard/sha256-f2606f6c7f4e1daf/preview.webp?v=sha256-f2606f6c7f4e1daf",
      "animationUrl": "https://edge.gift/gift-assets/astral_shard/sha256-f2606f6c7f4e1daf/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-b-day_candle",
    "telegramGiftId": "b-day_candle",
    "giftName": "b-day_candle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "b-day_candle",
      "previewUrl": "https://edge.gift/gift-assets/b-day_candle/sha256-1fc2e35ac35e5e86/preview.webp?v=sha256-1fc2e35ac35e5e86",
      "animationUrl": "https://edge.gift/gift-assets/b-day_candle/sha256-1fc2e35ac35e5e86/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-b_day_candle",
    "telegramGiftId": "b_day_candle",
    "giftName": "B Day Candle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "b_day_candle",
      "previewUrl": "https://edge.gift/gift-assets/b-day_candle/sha256-1fc2e35ac35e5e86/preview.webp?v=sha256-1fc2e35ac35e5e86%3Aalias-b_day_candle-20260614",
      "animationUrl": "https://edge.gift/gift-assets/b-day_candle/sha256-1fc2e35ac35e5e86/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-bear",
    "telegramGiftId": "bear",
    "giftName": "bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "bear",
      "previewUrl": "https://edge.gift/gift-assets/bear/sha256-b547d8b189822046/preview.webp?v=sha256-b547d8b189822046",
      "animationUrl": "https://edge.gift/gift-assets/bear/sha256-b547d8b189822046/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-berry_box",
    "telegramGiftId": "berry_box",
    "giftName": "berry_box",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "berry_box",
      "previewUrl": "https://edge.gift/gift-assets/berry_box/sha256-eb97733670b79cf0/preview.webp?v=sha256-eb97733670b79cf0",
      "animationUrl": "https://edge.gift/gift-assets/berry_box/sha256-eb97733670b79cf0/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-big_year",
    "telegramGiftId": "big_year",
    "giftName": "big_year",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "big_year",
      "previewUrl": "https://edge.gift/gift-assets/big_year/sha256-42a5a83d2b168c75/preview.webp?v=sha256-42a5a83d2b168c75",
      "animationUrl": "https://edge.gift/gift-assets/big_year/sha256-42a5a83d2b168c75/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-bling_binky",
    "telegramGiftId": "bling_binky",
    "giftName": "bling_binky",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "bling_binky",
      "previewUrl": "https://edge.gift/gift-assets/bling_binky/sha256-7f10fd36b15e3e4c/preview.png?v=sha256-7f10fd36b15e3e4c",
      "animationUrl": "https://edge.gift/gift-assets/bling_binky/sha256-7f10fd36b15e3e4c/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-bonded_ring",
    "telegramGiftId": "bonded_ring",
    "giftName": "bonded_ring",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "bonded_ring",
      "previewUrl": "https://edge.gift/gift-assets/bonded_ring/sha256-3f1e6c911cc0e00c/preview.webp?v=sha256-3f1e6c911cc0e00c",
      "animationUrl": "https://edge.gift/gift-assets/bonded_ring/sha256-3f1e6c911cc0e00c/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-bottle",
    "telegramGiftId": "bottle",
    "giftName": "bottle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "bottle",
      "previewUrl": "https://edge.gift/gift-assets/bottle/sha256-54b9bae7cd329ad0/preview.webp?v=sha256-54b9bae7cd329ad0",
      "animationUrl": "https://edge.gift/gift-assets/bottle/sha256-54b9bae7cd329ad0/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-bow_tie",
    "telegramGiftId": "bow_tie",
    "giftName": "bow_tie",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "bow_tie",
      "previewUrl": "https://edge.gift/gift-assets/bow_tie/sha256-d74cb317a9e4bc41/preview.webp?v=sha256-d74cb317a9e4bc41",
      "animationUrl": "https://edge.gift/gift-assets/bow_tie/sha256-d74cb317a9e4bc41/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-box",
    "telegramGiftId": "box",
    "giftName": "box",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "box",
      "previewUrl": "https://edge.gift/gift-assets/box/sha256-2a5fc30c40d96f47/preview.webp?v=sha256-2a5fc30c40d96f47",
      "animationUrl": "https://edge.gift/gift-assets/box/sha256-2a5fc30c40d96f47/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-bunny_muffin",
    "telegramGiftId": "bunny_muffin",
    "giftName": "bunny_muffin",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "bunny_muffin",
      "previewUrl": "https://edge.gift/gift-assets/bunny_muffin/sha256-696800c87ddbff4a/preview.webp?v=sha256-696800c87ddbff4a",
      "animationUrl": "https://edge.gift/gift-assets/bunny_muffin/sha256-696800c87ddbff4a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-cake",
    "telegramGiftId": "cake",
    "giftName": "cake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "cake",
      "previewUrl": "https://edge.gift/gift-assets/cake/sha256-a04ac93be8cfb7df/preview.webp?v=sha256-a04ac93be8cfb7df",
      "animationUrl": "https://edge.gift/gift-assets/cake/sha256-a04ac93be8cfb7df/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-candy_cane",
    "telegramGiftId": "candy_cane",
    "giftName": "candy_cane",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "candy_cane",
      "previewUrl": "https://edge.gift/gift-assets/candy_cane/sha256-d7a9431abd01bf2b/preview.webp?v=sha256-d7a9431abd01bf2b",
      "animationUrl": "https://edge.gift/gift-assets/candy_cane/sha256-d7a9431abd01bf2b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-car",
    "telegramGiftId": "car",
    "giftName": "car",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "car",
      "previewUrl": "https://edge.gift/gift-assets/car/sha256-d4033a5bc5b2aacb/preview.webp?v=sha256-d4033a5bc5b2aacb",
      "animationUrl": "https://edge.gift/gift-assets/car/sha256-d4033a5bc5b2aacb/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-chill_flame",
    "telegramGiftId": "chill_flame",
    "giftName": "chill_flame",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "chill_flame",
      "previewUrl": "https://edge.gift/gift-assets/chill_flame/sha256-7f07b83e064c908a/preview.png?v=sha256-7f07b83e064c908a",
      "animationUrl": "https://edge.gift/gift-assets/chill_flame/sha256-7f07b83e064c908a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-clover_pin",
    "telegramGiftId": "clover_pin",
    "giftName": "clover_pin",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "clover_pin",
      "previewUrl": "https://edge.gift/gift-assets/clover_pin/sha256-23c3b222098af73d/preview.webp?v=sha256-23c3b222098af73d",
      "animationUrl": "https://edge.gift/gift-assets/clover_pin/sha256-23c3b222098af73d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-coinGold",
    "telegramGiftId": "coinGold",
    "giftName": "Edge Gold",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "coinGold",
      "previewUrl": "https://edge.gift/gift-assets/coinGold/sha256-f40b4459769a34ed/preview.webp?v=sha256-f40b4459769a34ed",
      "animationUrl": "https://edge.gift/gift-assets/coinGold/sha256-f40b4459769a34ed/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-coinSilver",
    "telegramGiftId": "coinSilver",
    "giftName": "Edge Silver",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "coinSilver",
      "previewUrl": "https://edge.gift/gift-assets/coinSilver/sha256-7c375370af0299d7/preview.webp?v=sha256-7c375370af0299d7",
      "animationUrl": "https://edge.gift/gift-assets/coinSilver/sha256-7c375370af0299d7/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-cookie_heart",
    "telegramGiftId": "cookie_heart",
    "giftName": "cookie_heart",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "cookie_heart",
      "previewUrl": "https://edge.gift/gift-assets/cookie_heart/sha256-babd0e5c35b137e5/preview.webp?v=sha256-babd0e5c35b137e5",
      "animationUrl": "https://edge.gift/gift-assets/cookie_heart/sha256-babd0e5c35b137e5/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-crown",
    "telegramGiftId": "crown",
    "giftName": "crown",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "crown",
      "previewUrl": "https://edge.gift/gift-assets/crown/sha256-682151bd791dcf56/preview.webp?v=sha256-682151bd791dcf56",
      "animationUrl": "https://edge.gift/gift-assets/crown/sha256-682151bd791dcf56/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-crystal",
    "telegramGiftId": "crystal",
    "giftName": "crystal",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "crystal",
      "previewUrl": "https://edge.gift/gift-assets/crystal/sha256-af0d673cb76f2048/preview.webp?v=sha256-af0d673cb76f2048",
      "animationUrl": "https://edge.gift/gift-assets/crystal/sha256-af0d673cb76f2048/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-crystal_ball",
    "telegramGiftId": "crystal_ball",
    "giftName": "crystal_ball",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "crystal_ball",
      "previewUrl": "https://edge.gift/gift-assets/crystal_ball/sha256-b4dd7c2286dd79bc/preview.webp?v=sha256-b4dd7c2286dd79bc",
      "animationUrl": "https://edge.gift/gift-assets/crystal_ball/sha256-b4dd7c2286dd79bc/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-cup",
    "telegramGiftId": "cup",
    "giftName": "cup",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "cup",
      "previewUrl": "https://edge.gift/gift-assets/cup/sha256-dc7f6c8220607474/preview.webp?v=sha256-dc7f6c8220607474",
      "animationUrl": "https://edge.gift/gift-assets/cup/sha256-dc7f6c8220607474/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-cupid_charm",
    "telegramGiftId": "cupid_charm",
    "giftName": "cupid_charm",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "cupid_charm",
      "previewUrl": "https://edge.gift/gift-assets/cupid_charm/sha256-2e6ab4b6ea255d66/preview.webp?v=sha256-2e6ab4b6ea255d66",
      "animationUrl": "https://edge.gift/gift-assets/cupid_charm/sha256-2e6ab4b6ea255d66/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_bear",
    "telegramGiftId": "custom_bear",
    "giftName": "custom_bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_bear",
      "previewUrl": "https://edge.gift/gift-assets/custom_bear/sha256-7f8c59333cc15ecc/preview.webp?v=sha256-7f8c59333cc15ecc",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_bottle",
    "telegramGiftId": "custom_bottle",
    "giftName": "custom_bottle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_bottle",
      "previewUrl": "https://edge.gift/gift-assets/custom_bottle/sha256-491ffd1574552789/preview.webp?v=sha256-491ffd1574552789",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_box",
    "telegramGiftId": "custom_box",
    "giftName": "custom_box",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_box",
      "previewUrl": "https://edge.gift/gift-assets/custom_box/sha256-99e8c54e8f8826d8/preview.webp?v=sha256-99e8c54e8f8826d8",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_cake",
    "telegramGiftId": "custom_cake",
    "giftName": "custom_cake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_cake",
      "previewUrl": "https://edge.gift/gift-assets/custom_cake/sha256-cf9e4ad3da0af095/preview.webp?v=sha256-cf9e4ad3da0af095",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_crystal",
    "telegramGiftId": "custom_crystal",
    "giftName": "custom_crystal",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_crystal",
      "previewUrl": "https://edge.gift/gift-assets/custom_crystal/sha256-825a2f8274797ae9/preview.webp?v=sha256-825a2f8274797ae9",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_cup",
    "telegramGiftId": "custom_cup",
    "giftName": "custom_cup",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_cup",
      "previewUrl": "https://edge.gift/gift-assets/custom_cup/sha256-39898c3421e307b8/preview.webp?v=sha256-39898c3421e307b8",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_flowers",
    "telegramGiftId": "custom_flowers",
    "giftName": "custom_flowers",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_flowers",
      "previewUrl": "https://edge.gift/gift-assets/custom_flowers/sha256-5d26bd1ed265ca50/preview.webp?v=sha256-5d26bd1ed265ca50",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_heart",
    "telegramGiftId": "custom_heart",
    "giftName": "custom_heart",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_heart",
      "previewUrl": "https://edge.gift/gift-assets/custom_heart/sha256-92515367aa28a458/preview.webp?v=sha256-92515367aa28a458",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_ring",
    "telegramGiftId": "custom_ring",
    "giftName": "custom_ring",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_ring",
      "previewUrl": "https://edge.gift/gift-assets/custom_ring/sha256-091104e8b6050eba/preview.webp?v=sha256-091104e8b6050eba",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_rocket",
    "telegramGiftId": "custom_rocket",
    "giftName": "custom_rocket",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_rocket",
      "previewUrl": "https://edge.gift/gift-assets/custom_rocket/sha256-4171e153e6b61ea5/preview.webp?v=sha256-4171e153e6b61ea5",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-custom_rose",
    "telegramGiftId": "custom_rose",
    "giftName": "custom_rose",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "custom_rose",
      "previewUrl": "https://edge.gift/gift-assets/custom_rose/sha256-bd27f0bab8cc57be/preview.webp?v=sha256-bd27f0bab8cc57be",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-desk_calendar",
    "telegramGiftId": "desk_calendar",
    "giftName": "desk_calendar",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "desk_calendar",
      "previewUrl": "https://edge.gift/gift-assets/desk_calendar/sha256-1345a974d61069d3/preview.webp?v=sha256-1345a974d61069d3",
      "animationUrl": "https://edge.gift/gift-assets/desk_calendar/sha256-1345a974d61069d3/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-diamond",
    "telegramGiftId": "diamond",
    "giftName": "diamond",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "diamond",
      "previewUrl": "https://edge.gift/gift-assets/diamond/sha256-bdf78a755c1b708d/preview.webp?v=sha256-bdf78a755c1b708d",
      "animationUrl": "https://edge.gift/gift-assets/diamond/sha256-bdf78a755c1b708d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-diamond_ring",
    "telegramGiftId": "diamond_ring",
    "giftName": "diamond_ring",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "diamond_ring",
      "previewUrl": "https://edge.gift/gift-assets/diamond_ring/sha256-d53ce217a3d24640/preview.webp?v=sha256-d53ce217a3d24640",
      "animationUrl": "https://edge.gift/gift-assets/diamond_ring/sha256-d53ce217a3d24640/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-durovs_cap",
    "telegramGiftId": "durovs_cap",
    "giftName": "durovs_cap",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "durovs_cap",
      "previewUrl": "https://edge.gift/gift-assets/durovs_cap/sha256-4aa57447658bbcfb/preview.webp?v=sha256-4aa57447658bbcfb",
      "animationUrl": "https://edge.gift/gift-assets/durovs_cap/sha256-4aa57447658bbcfb/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-durovs_glasses",
    "telegramGiftId": "durovs_glasses",
    "giftName": "Durov's Glasses",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "durovs_glasses",
      "previewUrl": "https://edge.gift/gift-assets/durovs_glasses/changes-232151b3ab3e-e541edb1/preview.png?v=changes-232151b3ab3e-e541edb1",
      "animationUrl": "https://edge.gift/gift-assets/durovs_glasses/changes-232151b3ab3e-e541edb1/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-easter_egg",
    "telegramGiftId": "easter_egg",
    "giftName": "easter_egg",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "easter_egg",
      "previewUrl": "https://edge.gift/gift-assets/easter_egg/sha256-235c827a625544d1/preview.webp?v=sha256-235c827a625544d1",
      "animationUrl": "https://edge.gift/gift-assets/easter_egg/sha256-235c827a625544d1/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-electric_skull",
    "telegramGiftId": "electric_skull",
    "giftName": "electric_skull",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "electric_skull",
      "previewUrl": "https://edge.gift/gift-assets/electric_skull/sha256-4b2411b1dbfbeb96/preview.webp?v=sha256-4b2411b1dbfbeb96",
      "animationUrl": "https://edge.gift/gift-assets/electric_skull/sha256-4b2411b1dbfbeb96/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-eternal_candle",
    "telegramGiftId": "eternal_candle",
    "giftName": "eternal_candle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "eternal_candle",
      "previewUrl": "https://edge.gift/gift-assets/eternal_candle/sha256-7687e95b00523474/preview.webp?v=sha256-7687e95b00523474",
      "animationUrl": "https://edge.gift/gift-assets/eternal_candle/sha256-7687e95b00523474/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-eternal_rose",
    "telegramGiftId": "eternal_rose",
    "giftName": "eternal_rose",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "eternal_rose",
      "previewUrl": "https://edge.gift/gift-assets/eternal_rose/sha256-8f3bed6f7dd770e0/preview.webp?v=sha256-8f3bed6f7dd770e0",
      "animationUrl": "https://edge.gift/gift-assets/eternal_rose/sha256-8f3bed6f7dd770e0/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-evil_eye",
    "telegramGiftId": "evil_eye",
    "giftName": "evil_eye",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "evil_eye",
      "previewUrl": "https://edge.gift/gift-assets/evil_eye/sha256-830649f1bdaa2690/preview.webp?v=sha256-830649f1bdaa2690",
      "animationUrl": "https://edge.gift/gift-assets/evil_eye/sha256-830649f1bdaa2690/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-faith_amulet",
    "telegramGiftId": "faith_amulet",
    "giftName": "faith_amulet",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "faith_amulet",
      "previewUrl": "https://edge.gift/gift-assets/faith_amulet/sha256-8f2dd76b195964ad/preview.webp?v=sha256-8f2dd76b195964ad",
      "animationUrl": "https://edge.gift/gift-assets/faith_amulet/sha256-8f2dd76b195964ad/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-fine_pen",
    "telegramGiftId": "fine_pen",
    "giftName": "Fine Pen",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "fine_pen",
      "previewUrl": "https://edge.gift/gift-assets/fine_pen/changes-ab730b68bf6d-d5180922/preview.png?v=changes-ab730b68bf6d-d5180922",
      "animationUrl": "https://edge.gift/gift-assets/fine_pen/changes-ab730b68bf6d-d5180922/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-flowers",
    "telegramGiftId": "flowers",
    "giftName": "flowers",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "flowers",
      "previewUrl": "https://edge.gift/gift-assets/flowers/sha256-9df1852ad3b61b21/preview.webp?v=sha256-9df1852ad3b61b21",
      "animationUrl": "https://edge.gift/gift-assets/flowers/sha256-9df1852ad3b61b21/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-flying_broom",
    "telegramGiftId": "flying_broom",
    "giftName": "flying_broom",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "flying_broom",
      "previewUrl": "https://edge.gift/gift-assets/flying_broom/sha256-3c6a64cf06c722b7/preview.webp?v=sha256-3c6a64cf06c722b7",
      "animationUrl": "https://edge.gift/gift-assets/flying_broom/sha256-3c6a64cf06c722b7/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-fresh_socks",
    "telegramGiftId": "fresh_socks",
    "giftName": "fresh_socks",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "fresh_socks",
      "previewUrl": "https://edge.gift/gift-assets/fresh_socks/sha256-cf99147620765392/preview.webp?v=sha256-cf99147620765392",
      "animationUrl": "https://edge.gift/gift-assets/fresh_socks/sha256-cf99147620765392/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-gem_signet",
    "telegramGiftId": "gem_signet",
    "giftName": "gem_signet",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "gem_signet",
      "previewUrl": "https://edge.gift/gift-assets/gem_signet/sha256-28e0b84e8b526ae2/preview.webp?v=sha256-28e0b84e8b526ae2",
      "animationUrl": "https://edge.gift/gift-assets/gem_signet/sha256-28e0b84e8b526ae2/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-genie_lamp",
    "telegramGiftId": "genie_lamp",
    "giftName": "genie_lamp",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "genie_lamp",
      "previewUrl": "https://edge.gift/gift-assets/genie_lamp/sha256-19e642a474279b46/preview.webp?v=sha256-19e642a474279b46",
      "animationUrl": "https://edge.gift/gift-assets/genie_lamp/sha256-19e642a474279b46/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-ginger_cookie",
    "telegramGiftId": "ginger_cookie",
    "giftName": "ginger_cookie",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "ginger_cookie",
      "previewUrl": "https://edge.gift/gift-assets/ginger_cookie/sha256-9214b9f091d231b6/preview.webp?v=sha256-9214b9f091d231b6",
      "animationUrl": "https://edge.gift/gift-assets/ginger_cookie/sha256-9214b9f091d231b6/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-hanging_star",
    "telegramGiftId": "hanging_star",
    "giftName": "hanging_star",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "hanging_star",
      "previewUrl": "https://edge.gift/gift-assets/hanging_star/sha256-3f00ba9873e9c079/preview.webp?v=sha256-3f00ba9873e9c079",
      "animationUrl": "https://edge.gift/gift-assets/hanging_star/sha256-3f00ba9873e9c079/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-happy_brownie",
    "telegramGiftId": "happy_brownie",
    "giftName": "happy_brownie",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "happy_brownie",
      "previewUrl": "https://edge.gift/gift-assets/happy_brownie/sha256-2a9fb982fc73bf36/preview.webp?v=sha256-2a9fb982fc73bf36",
      "animationUrl": "https://edge.gift/gift-assets/happy_brownie/sha256-2a9fb982fc73bf36/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-heart",
    "telegramGiftId": "heart",
    "giftName": "heart",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "heart",
      "previewUrl": "https://edge.gift/gift-assets/heart/sha256-b8f8c6e4eb5b6ccf/preview.webp?v=sha256-b8f8c6e4eb5b6ccf",
      "animationUrl": "https://edge.gift/gift-assets/heart/sha256-b8f8c6e4eb5b6ccf/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-heart_locket",
    "telegramGiftId": "heart_locket",
    "giftName": "heart_locket",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "heart_locket",
      "previewUrl": "https://edge.gift/gift-assets/heart_locket/sha256-d1fb77573b65c9a8/preview.webp?v=sha256-d1fb77573b65c9a8",
      "animationUrl": "https://edge.gift/gift-assets/heart_locket/sha256-d1fb77573b65c9a8/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-heroic_helmet",
    "telegramGiftId": "heroic_helmet",
    "giftName": "heroic_helmet",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "heroic_helmet",
      "previewUrl": "https://edge.gift/gift-assets/heroic_helmet/sha256-45448d40673cb233/preview.webp?v=sha256-45448d40673cb233",
      "animationUrl": "https://edge.gift/gift-assets/heroic_helmet/sha256-45448d40673cb233/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-hex_pot",
    "telegramGiftId": "hex_pot",
    "giftName": "hex_pot",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "hex_pot",
      "previewUrl": "https://edge.gift/gift-assets/hex_pot/sha256-1d8b783e1f96727c/preview.webp?v=sha256-1d8b783e1f96727c",
      "animationUrl": "https://edge.gift/gift-assets/hex_pot/sha256-1d8b783e1f96727c/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-holiday_drink",
    "telegramGiftId": "holiday_drink",
    "giftName": "holiday_drink",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "holiday_drink",
      "previewUrl": "https://edge.gift/gift-assets/holiday_drink/sha256-ef0c1fc31485fcac/preview.webp?v=sha256-ef0c1fc31485fcac",
      "animationUrl": "https://edge.gift/gift-assets/holiday_drink/sha256-ef0c1fc31485fcac/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-homemade_cake",
    "telegramGiftId": "homemade_cake",
    "giftName": "homemade_cake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "homemade_cake",
      "previewUrl": "https://edge.gift/gift-assets/homemade_cake/sha256-af1b9d99286eb0b3/preview.webp?v=sha256-af1b9d99286eb0b3",
      "animationUrl": "https://edge.gift/gift-assets/homemade_cake/sha256-af1b9d99286eb0b3/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-hypno_lollipop",
    "telegramGiftId": "hypno_lollipop",
    "giftName": "hypno_lollipop",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "hypno_lollipop",
      "previewUrl": "https://edge.gift/gift-assets/hypno_lollipop/sha256-80c27ed03f572717/preview.webp?v=sha256-80c27ed03f572717",
      "animationUrl": "https://edge.gift/gift-assets/hypno_lollipop/sha256-80c27ed03f572717/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-ice_cream",
    "telegramGiftId": "ice_cream",
    "giftName": "ice_cream",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "ice_cream",
      "previewUrl": "https://edge.gift/gift-assets/ice_cream/sha256-6f4c4a9bcf4d0aab/preview.webp?v=sha256-6f4c4a9bcf4d0aab",
      "animationUrl": "https://edge.gift/gift-assets/ice_cream/sha256-6f4c4a9bcf4d0aab/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-input_key",
    "telegramGiftId": "input_key",
    "giftName": "input_key",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "input_key",
      "previewUrl": "https://edge.gift/gift-assets/input_key/sha256-89b6382c316fbff9/preview.webp?v=sha256-89b6382c316fbff9",
      "animationUrl": "https://edge.gift/gift-assets/input_key/sha256-89b6382c316fbff9/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-instant_ramen",
    "telegramGiftId": "instant_ramen",
    "giftName": "instant_ramen",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "instant_ramen",
      "previewUrl": "https://edge.gift/gift-assets/instant_ramen/sha256-8084c4b22565005b/preview.webp?v=sha256-8084c4b22565005b",
      "animationUrl": "https://edge.gift/gift-assets/instant_ramen/sha256-8084c4b22565005b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-ion_gem",
    "telegramGiftId": "ion_gem",
    "giftName": "ion_gem",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "ion_gem",
      "previewUrl": "https://edge.gift/gift-assets/ion_gem/sha256-2ab6fddb2ecb8d7b/preview.webp?v=sha256-2ab6fddb2ecb8d7b",
      "animationUrl": "https://edge.gift/gift-assets/ion_gem/sha256-2ab6fddb2ecb8d7b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-ionic_dryer",
    "telegramGiftId": "ionic_dryer",
    "giftName": "ionic_dryer",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "ionic_dryer",
      "previewUrl": "https://edge.gift/gift-assets/ionic_dryer/sha256-27dd5511351f202f/preview.webp?v=sha256-27dd5511351f202f",
      "animationUrl": "https://edge.gift/gift-assets/ionic_dryer/sha256-27dd5511351f202f/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-jack-in-the-box",
    "telegramGiftId": "jack-in-the-box",
    "giftName": "jack-in-the-box",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "jack-in-the-box",
      "previewUrl": "https://edge.gift/gift-assets/jack-in-the-box/sha256-001f6e7fc48a3dc7/preview.webp?v=sha256-001f6e7fc48a3dc7",
      "animationUrl": "https://edge.gift/gift-assets/jack-in-the-box/sha256-001f6e7fc48a3dc7/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-jelly_bunny",
    "telegramGiftId": "jelly_bunny",
    "giftName": "jelly_bunny",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "jelly_bunny",
      "previewUrl": "https://edge.gift/gift-assets/jelly_bunny/sha256-5dc309d89505a84b/preview.webp?v=sha256-5dc309d89505a84b",
      "animationUrl": "https://edge.gift/gift-assets/jelly_bunny/sha256-5dc309d89505a84b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-jester_hat",
    "telegramGiftId": "jester_hat",
    "giftName": "jester_hat",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "jester_hat",
      "previewUrl": "https://edge.gift/gift-assets/jester_hat/sha256-6b16944f259bad08/preview.webp?v=sha256-6b16944f259bad08",
      "animationUrl": "https://edge.gift/gift-assets/jester_hat/sha256-6b16944f259bad08/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-jingle_bells",
    "telegramGiftId": "jingle_bells",
    "giftName": "jingle_bells",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "jingle_bells",
      "previewUrl": "https://edge.gift/gift-assets/jingle_bells/sha256-bc7e9565d6416833/preview.webp?v=sha256-bc7e9565d6416833",
      "animationUrl": "https://edge.gift/gift-assets/jingle_bells/sha256-bc7e9565d6416833/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-jolly_chimp",
    "telegramGiftId": "jolly_chimp",
    "giftName": "jolly_chimp",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "jolly_chimp",
      "previewUrl": "https://edge.gift/gift-assets/jolly_chimp/sha256-e1a9efb9267561d4/preview.webp?v=sha256-e1a9efb9267561d4",
      "animationUrl": "https://edge.gift/gift-assets/jolly_chimp/sha256-e1a9efb9267561d4/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-joyful_bundle",
    "telegramGiftId": "joyful_bundle",
    "giftName": "joyful_bundle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "joyful_bundle",
      "previewUrl": "https://edge.gift/gift-assets/joyful_bundle/sha256-9f76801e538688e5/preview.webp?v=sha256-9f76801e538688e5",
      "animationUrl": "https://edge.gift/gift-assets/joyful_bundle/sha256-9f76801e538688e5/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-khabibs_papakha",
    "telegramGiftId": "khabibs_papakha",
    "giftName": "khabibs_papakha",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "khabibs_papakha",
      "previewUrl": "https://edge.gift/gift-assets/khabibs_papakha/sha256-9a5e4f5063fec18f/preview.png?v=sha256-9a5e4f5063fec18f",
      "animationUrl": "https://edge.gift/gift-assets/khabibs_papakha/sha256-9a5e4f5063fec18f/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-kissed_frog",
    "telegramGiftId": "kissed_frog",
    "giftName": "kissed_frog",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "kissed_frog",
      "previewUrl": "https://edge.gift/gift-assets/kissed_frog/sha256-383dc58ccd07bd73/preview.webp?v=sha256-383dc58ccd07bd73",
      "animationUrl": "https://edge.gift/gift-assets/kissed_frog/sha256-383dc58ccd07bd73/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-liberty_figure",
    "telegramGiftId": "liberty_figure",
    "giftName": "Liberty Figure",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "liberty_figure",
      "previewUrl": "https://edge.gift/gift-assets/liberty_figure/changes-9d2f7ecf62f4-aee07444/preview.png?v=changes-9d2f7ecf62f4-aee07444",
      "animationUrl": "https://edge.gift/gift-assets/liberty_figure/changes-9d2f7ecf62f4-aee07444/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-light_sword",
    "telegramGiftId": "light_sword",
    "giftName": "light_sword",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "light_sword",
      "previewUrl": "https://edge.gift/gift-assets/light_sword/sha256-2e8e91d52375ea01/preview.webp?v=sha256-2e8e91d52375ea01",
      "animationUrl": "https://edge.gift/gift-assets/light_sword/sha256-2e8e91d52375ea01/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-lol_pop",
    "telegramGiftId": "lol_pop",
    "giftName": "lol_pop",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "lol_pop",
      "previewUrl": "https://edge.gift/gift-assets/lol_pop/sha256-3b870bb49ded6bdd/preview.webp?v=sha256-3b870bb49ded6bdd",
      "animationUrl": "https://edge.gift/gift-assets/lol_pop/sha256-3b870bb49ded6bdd/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-lollipop",
    "telegramGiftId": "lollipop",
    "giftName": "lollipop",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "lollipop",
      "previewUrl": "https://edge.gift/gift-assets/lollipop/sha256-546f6db0d88004d0/preview.webp?v=sha256-546f6db0d88004d0",
      "animationUrl": "https://edge.gift/gift-assets/lollipop/sha256-546f6db0d88004d0/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-lootPackPreview",
    "telegramGiftId": "lootPackPreview",
    "giftName": "Loot Pack Preview",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "lootPackPreview",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_bag",
    "telegramGiftId": "loot_bag",
    "giftName": "loot_bag",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_bag",
      "previewUrl": "https://edge.gift/gift-assets/loot_bag/sha256-0d320ecf33498e64/preview.webp?v=sha256-0d320ecf33498e64",
      "animationUrl": "https://edge.gift/gift-assets/loot_bag/sha256-0d320ecf33498e64/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_gold_100",
    "telegramGiftId": "loot_pack_gold_100",
    "giftName": "Common Gold Pack",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_gold_100",
      "previewUrl": "https://edge.gift/gift-assets/loot_pack_silver_50/sha256-138002c1cea26358/preview.png?v=farm-gold-pack-v1",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_gold_20000",
    "telegramGiftId": "loot_pack_gold_20000",
    "giftName": "Legendary Gold Pack 20000",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_gold_20000",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_gold_2500",
    "telegramGiftId": "loot_pack_gold_2500",
    "giftName": "Epic Gold Pack 2500",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_gold_2500",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_gold_500",
    "telegramGiftId": "loot_pack_gold_500",
    "giftName": "Rare Gold Pack",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_gold_500",
      "previewUrl": "https://edge.gift/gift-assets/loot_pack_silver_50/sha256-138002c1cea26358/preview.png?v=farm-gold-pack-v1",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_gold_50000",
    "telegramGiftId": "loot_pack_gold_50000",
    "giftName": "Superior Gold Pack 50000",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_gold_50000",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_gold_7500",
    "telegramGiftId": "loot_pack_gold_7500",
    "giftName": "Mythic Gold Pack",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_gold_7500",
      "previewUrl": "https://edge.gift/gift-assets/loot_pack_silver_50/sha256-138002c1cea26358/preview.png?v=farm-gold-pack-v1",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_silver_100",
    "telegramGiftId": "loot_pack_silver_100",
    "giftName": "Common Silver Pack 100",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_silver_100",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_silver_20000",
    "telegramGiftId": "loot_pack_silver_20000",
    "giftName": "Legendary Silver Pack 20000",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_silver_20000",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_silver_2500",
    "telegramGiftId": "loot_pack_silver_2500",
    "giftName": "Epic Silver Pack 2500",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_silver_2500",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_silver_50",
    "telegramGiftId": "loot_pack_silver_50",
    "giftName": "Support Pack",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_silver_50",
      "previewUrl": "https://edge.gift/gift-assets/loot_pack_silver_50/sha256-138002c1cea26358/preview.png?v=loot-pack-support-v1",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_silver_500",
    "telegramGiftId": "loot_pack_silver_500",
    "giftName": "Rare Silver Pack 500",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_silver_500",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_silver_50000",
    "telegramGiftId": "loot_pack_silver_50000",
    "giftName": "Superior Silver Pack 50000",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_silver_50000",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_silver_7500",
    "telegramGiftId": "loot_pack_silver_7500",
    "giftName": "Mythic Silver Pack 7500",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_silver_7500",
      "previewUrl": "https://edge.gift/gift-assets/lootPackPreview/sha256-65db0e8dcd02f1e4/preview.png?v=sha256-65db0e8dcd02f1e4",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-loot_pack_vip_300",
    "telegramGiftId": "loot_pack_vip_300",
    "giftName": "VIP Pack",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "loot_pack_vip_300",
      "previewUrl": "https://edge.gift/gift-assets/loot_pack_vip_300/sha256-37db9647a93035bc/preview.png?v=loot-pack-vip-v1",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-love_candle",
    "telegramGiftId": "love_candle",
    "giftName": "love_candle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "love_candle",
      "previewUrl": "https://edge.gift/gift-assets/love_candle/sha256-aeec977415ec274e/preview.webp?v=sha256-aeec977415ec274e",
      "animationUrl": "https://edge.gift/gift-assets/love_candle/sha256-aeec977415ec274e/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-love_potion",
    "telegramGiftId": "love_potion",
    "giftName": "love_potion",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "love_potion",
      "previewUrl": "https://edge.gift/gift-assets/love_potion/sha256-aa9893a082868342/preview.webp?v=sha256-aa9893a082868342",
      "animationUrl": "https://edge.gift/gift-assets/love_potion/sha256-aa9893a082868342/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-low_rider",
    "telegramGiftId": "low_rider",
    "giftName": "low_rider",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "low_rider",
      "previewUrl": "https://edge.gift/gift-assets/low_rider/sha256-619ad547ccf1b680/preview.webp?v=sha256-619ad547ccf1b680",
      "animationUrl": "https://edge.gift/gift-assets/low_rider/sha256-619ad547ccf1b680/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-lucky_bear",
    "telegramGiftId": "lucky_bear",
    "giftName": "lucky_bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "lucky_bear",
      "previewUrl": "https://edge.gift/gift-assets/lucky_bear/sha256-1485e5e7ebca22a2/preview.webp?v=sha256-1485e5e7ebca22a2",
      "animationUrl": "",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-lunar_snake",
    "telegramGiftId": "lunar_snake",
    "giftName": "lunar_snake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "lunar_snake",
      "previewUrl": "https://edge.gift/gift-assets/lunar_snake/sha256-8af2ead6d9d2384d/preview.webp?v=sha256-8af2ead6d9d2384d",
      "animationUrl": "https://edge.gift/gift-assets/lunar_snake/sha256-8af2ead6d9d2384d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-lush_bouquet",
    "telegramGiftId": "lush_bouquet",
    "giftName": "lush_bouquet",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "lush_bouquet",
      "previewUrl": "https://edge.gift/gift-assets/lush_bouquet/sha256-3377dacfe0d9c97b/preview.webp?v=sha256-3377dacfe0d9c97b",
      "animationUrl": "https://edge.gift/gift-assets/lush_bouquet/sha256-3377dacfe0d9c97b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-mad_pumpkin",
    "telegramGiftId": "mad_pumpkin",
    "giftName": "mad_pumpkin",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "mad_pumpkin",
      "previewUrl": "https://edge.gift/gift-assets/mad_pumpkin/sha256-e59a2c70fb221ffc/preview.webp?v=sha256-e59a2c70fb221ffc",
      "animationUrl": "https://edge.gift/gift-assets/mad_pumpkin/sha256-e59a2c70fb221ffc/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-magic_potion",
    "telegramGiftId": "magic_potion",
    "giftName": "magic_potion",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "magic_potion",
      "previewUrl": "https://edge.gift/gift-assets/magic_potion/sha256-4f1e12597fff9c6d/preview.webp?v=sha256-4f1e12597fff9c6d",
      "animationUrl": "https://edge.gift/gift-assets/magic_potion/sha256-4f1e12597fff9c6d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-mighty_arm",
    "telegramGiftId": "mighty_arm",
    "giftName": "mighty_arm",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "mighty_arm",
      "previewUrl": "https://edge.gift/gift-assets/mighty_arm/sha256-efc72360c5c80c96/preview.webp?v=sha256-efc72360c5c80c96",
      "animationUrl": "https://edge.gift/gift-assets/mighty_arm/sha256-efc72360c5c80c96/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-mini_oscar",
    "telegramGiftId": "mini_oscar",
    "giftName": "mini_oscar",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "mini_oscar",
      "previewUrl": "https://edge.gift/gift-assets/mini_oscar/sha256-c7aa2f9f6255778d/preview.webp?v=sha256-c7aa2f9f6255778d",
      "animationUrl": "https://edge.gift/gift-assets/mini_oscar/sha256-c7aa2f9f6255778d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-money_pot",
    "telegramGiftId": "money_pot",
    "giftName": "money_pot",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "money_pot",
      "previewUrl": "https://edge.gift/gift-assets/money_pot/sha256-0c0423774dd9fe81/preview.png?v=sha256-0c0423774dd9fe81",
      "animationUrl": "https://edge.gift/gift-assets/money_pot/sha256-0c0423774dd9fe81/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-mood_pack",
    "telegramGiftId": "mood_pack",
    "giftName": "mood_pack",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "mood_pack",
      "previewUrl": "https://edge.gift/gift-assets/mood_pack/sha256-011821a39fa346c9/preview.png?v=sha256-011821a39fa346c9",
      "animationUrl": "https://edge.gift/gift-assets/mood_pack/sha256-011821a39fa346c9/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-moon_pendant",
    "telegramGiftId": "moon_pendant",
    "giftName": "moon_pendant",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "moon_pendant",
      "previewUrl": "https://edge.gift/gift-assets/moon_pendant/sha256-312eda27f088d3db/preview.webp?v=sha256-312eda27f088d3db",
      "animationUrl": "https://edge.gift/gift-assets/moon_pendant/sha256-312eda27f088d3db/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-mousse_cake",
    "telegramGiftId": "mousse_cake",
    "giftName": "mousse_cake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "mousse_cake",
      "previewUrl": "https://edge.gift/gift-assets/mousse_cake/sha256-8c5696e945315a4e/preview.webp?v=sha256-8c5696e945315a4e",
      "animationUrl": "https://edge.gift/gift-assets/mousse_cake/sha256-8c5696e945315a4e/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-nail_bracelet",
    "telegramGiftId": "nail_bracelet",
    "giftName": "nail_bracelet",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "nail_bracelet",
      "previewUrl": "https://edge.gift/gift-assets/nail_bracelet/sha256-ede3437220f08663/preview.webp?v=sha256-ede3437220f08663",
      "animationUrl": "https://edge.gift/gift-assets/nail_bracelet/sha256-ede3437220f08663/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-neko_helmet",
    "telegramGiftId": "neko_helmet",
    "giftName": "neko_helmet",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "neko_helmet",
      "previewUrl": "https://edge.gift/gift-assets/neko_helmet/sha256-9d2b6e5d102d1f50/preview.webp?v=sha256-9d2b6e5d102d1f50",
      "animationUrl": "https://edge.gift/gift-assets/neko_helmet/sha256-9d2b6e5d102d1f50/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-party_sparkler",
    "telegramGiftId": "party_sparkler",
    "giftName": "party_sparkler",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "party_sparkler",
      "previewUrl": "https://edge.gift/gift-assets/party_sparkler/sha256-20673066124bd104/preview.webp?v=sha256-20673066124bd104",
      "animationUrl": "https://edge.gift/gift-assets/party_sparkler/sha256-20673066124bd104/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-perfume_bottle",
    "telegramGiftId": "perfume_bottle",
    "giftName": "perfume_bottle",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "perfume_bottle",
      "previewUrl": "https://edge.gift/gift-assets/perfume_bottle/sha256-1d494a166d84455b/preview.webp?v=sha256-1d494a166d84455b",
      "animationUrl": "https://edge.gift/gift-assets/perfume_bottle/sha256-1d494a166d84455b/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-pet_snake",
    "telegramGiftId": "pet_snake",
    "giftName": "pet_snake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "pet_snake",
      "previewUrl": "https://edge.gift/gift-assets/pet_snake/sha256-122f4b2677460083/preview.webp?v=sha256-122f4b2677460083",
      "animationUrl": "https://edge.gift/gift-assets/pet_snake/sha256-122f4b2677460083/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-plush_pepe",
    "telegramGiftId": "plush_pepe",
    "giftName": "plush_pepe",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "plush_pepe",
      "previewUrl": "https://edge.gift/gift-assets/plush_pepe/sha256-c1f3a02ed8ac7924/preview.webp?v=sha256-c1f3a02ed8ac7924",
      "animationUrl": "https://edge.gift/gift-assets/plush_pepe/sha256-c1f3a02ed8ac7924/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-pool_float",
    "telegramGiftId": "pool_float",
    "giftName": "pool_float",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "pool_float",
      "previewUrl": "https://edge.gift/gift-assets/pool_float/sha256-785925339e31bf0a/preview.png?v=sha256-785925339e31bf0a",
      "animationUrl": "https://edge.gift/gift-assets/pool_float/sha256-785925339e31bf0a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-precious_peach",
    "telegramGiftId": "precious_peach",
    "giftName": "precious_peach",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "precious_peach",
      "previewUrl": "https://edge.gift/gift-assets/precious_peach/sha256-b4c4a2625ee72a87/preview.webp?v=sha256-b4c4a2625ee72a87",
      "animationUrl": "https://edge.gift/gift-assets/precious_peach/sha256-b4c4a2625ee72a87/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-pretty_posy",
    "telegramGiftId": "pretty_posy",
    "giftName": "pretty_posy",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "pretty_posy",
      "previewUrl": "https://edge.gift/gift-assets/pretty_posy/sha256-742745759fae4e1e/preview.png?v=sha256-742745759fae4e1e",
      "animationUrl": "https://edge.gift/gift-assets/pretty_posy/sha256-742745759fae4e1e/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-rare_bird",
    "telegramGiftId": "rare_bird",
    "giftName": "rare_bird",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "rare_bird",
      "previewUrl": "https://edge.gift/gift-assets/rare_bird/sha256-2b6f7d48f8c13ce1/preview.png?v=sha256-2b6f7d48f8c13ce1",
      "animationUrl": "https://edge.gift/gift-assets/rare_bird/sha256-2b6f7d48f8c13ce1/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-record_player",
    "telegramGiftId": "record_player",
    "giftName": "record_player",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "record_player",
      "previewUrl": "https://edge.gift/gift-assets/record_player/sha256-31df6ca3e529c55f/preview.webp?v=sha256-31df6ca3e529c55f",
      "animationUrl": "https://edge.gift/gift-assets/record_player/sha256-31df6ca3e529c55f/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-restless_jar",
    "telegramGiftId": "restless_jar",
    "giftName": "restless_jar",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "restless_jar",
      "previewUrl": "https://edge.gift/gift-assets/restless_jar/sha256-0c3426e57b6933e4/preview.webp?v=sha256-0c3426e57b6933e4",
      "animationUrl": "https://edge.gift/gift-assets/restless_jar/sha256-0c3426e57b6933e4/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-ring",
    "telegramGiftId": "ring",
    "giftName": "ring",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "ring",
      "previewUrl": "https://edge.gift/gift-assets/ring/sha256-9d6ffba123ec8b01/preview.webp?v=sha256-9d6ffba123ec8b01",
      "animationUrl": "https://edge.gift/gift-assets/ring/sha256-9d6ffba123ec8b01/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-rocket",
    "telegramGiftId": "rocket",
    "giftName": "rocket",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "rocket",
      "previewUrl": "https://edge.gift/gift-assets/rocket/sha256-fcffaa0091f522ad/preview.webp?v=sha256-fcffaa0091f522ad",
      "animationUrl": "https://edge.gift/gift-assets/rocket/sha256-fcffaa0091f522ad/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-rose",
    "telegramGiftId": "rose",
    "giftName": "rose",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "rose",
      "previewUrl": "https://edge.gift/gift-assets/rose/sha256-553e818cd72c5a81/preview.webp?v=sha256-553e818cd72c5a81",
      "animationUrl": "https://edge.gift/gift-assets/rose/sha256-553e818cd72c5a81/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-sakura_flower",
    "telegramGiftId": "sakura_flower",
    "giftName": "sakura_flower",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "sakura_flower",
      "previewUrl": "https://edge.gift/gift-assets/sakura_flower/sha256-267722144ead2254/preview.webp?v=sha256-267722144ead2254",
      "animationUrl": "https://edge.gift/gift-assets/sakura_flower/sha256-267722144ead2254/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-santa_hat",
    "telegramGiftId": "santa_hat",
    "giftName": "santa_hat",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "santa_hat",
      "previewUrl": "https://edge.gift/gift-assets/santa_hat/sha256-19777bfdd12b7f7f/preview.webp?v=sha256-19777bfdd12b7f7f",
      "animationUrl": "https://edge.gift/gift-assets/santa_hat/sha256-19777bfdd12b7f7f/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-scared_cat",
    "telegramGiftId": "scared_cat",
    "giftName": "scared_cat",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "scared_cat",
      "previewUrl": "https://edge.gift/gift-assets/scared_cat/sha256-0ded9db602f3c7b1/preview.webp?v=sha256-0ded9db602f3c7b1",
      "animationUrl": "https://edge.gift/gift-assets/scared_cat/sha256-0ded9db602f3c7b1/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-sharp_tongue",
    "telegramGiftId": "sharp_tongue",
    "giftName": "sharp_tongue",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "sharp_tongue",
      "previewUrl": "https://edge.gift/gift-assets/sharp_tongue/sha256-6a46b85b1e2fbe18/preview.webp?v=sha256-6a46b85b1e2fbe18",
      "animationUrl": "https://edge.gift/gift-assets/sharp_tongue/sha256-6a46b85b1e2fbe18/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-signet_ring",
    "telegramGiftId": "signet_ring",
    "giftName": "signet_ring",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "signet_ring",
      "previewUrl": "https://edge.gift/gift-assets/signet_ring/sha256-26065fb45b2861ee/preview.webp?v=sha256-26065fb45b2861ee",
      "animationUrl": "https://edge.gift/gift-assets/signet_ring/sha256-26065fb45b2861ee/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-skull_flower",
    "telegramGiftId": "skull_flower",
    "giftName": "skull_flower",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "skull_flower",
      "previewUrl": "https://edge.gift/gift-assets/skull_flower/sha256-6eef66a9c93ec4ac/preview.webp?v=sha256-6eef66a9c93ec4ac",
      "animationUrl": "https://edge.gift/gift-assets/skull_flower/sha256-6eef66a9c93ec4ac/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-sky_stilettos",
    "telegramGiftId": "sky_stilettos",
    "giftName": "sky_stilettos",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "sky_stilettos",
      "previewUrl": "https://edge.gift/gift-assets/sky_stilettos/sha256-d16147508c3dc6c6/preview.webp?v=sha256-d16147508c3dc6c6",
      "animationUrl": "https://edge.gift/gift-assets/sky_stilettos/sha256-d16147508c3dc6c6/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-sleigh_bell",
    "telegramGiftId": "sleigh_bell",
    "giftName": "sleigh_bell",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "sleigh_bell",
      "previewUrl": "https://edge.gift/gift-assets/sleigh_bell/sha256-50ece37a565b86a5/preview.webp?v=sha256-50ece37a565b86a5",
      "animationUrl": "https://edge.gift/gift-assets/sleigh_bell/sha256-50ece37a565b86a5/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-snake_box",
    "telegramGiftId": "snake_box",
    "giftName": "snake_box",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "snake_box",
      "previewUrl": "https://edge.gift/gift-assets/snake_box/sha256-223e2d8eed7663e2/preview.webp?v=sha256-223e2d8eed7663e2",
      "animationUrl": "https://edge.gift/gift-assets/snake_box/sha256-223e2d8eed7663e2/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-snoop_cigar",
    "telegramGiftId": "snoop_cigar",
    "giftName": "snoop_cigar",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "snoop_cigar",
      "previewUrl": "https://edge.gift/gift-assets/snoop_cigar/sha256-13b2bd4093eadbb5/preview.webp?v=sha256-13b2bd4093eadbb5",
      "animationUrl": "https://edge.gift/gift-assets/snoop_cigar/sha256-13b2bd4093eadbb5/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-snoop_dogg",
    "telegramGiftId": "snoop_dogg",
    "giftName": "snoop_dogg",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "snoop_dogg",
      "previewUrl": "https://edge.gift/gift-assets/snoop_dogg/sha256-db3f51ee30c47fe7/preview.webp?v=sha256-db3f51ee30c47fe7",
      "animationUrl": "https://edge.gift/gift-assets/snoop_dogg/sha256-db3f51ee30c47fe7/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-snow_globe",
    "telegramGiftId": "snow_globe",
    "giftName": "snow_globe",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "snow_globe",
      "previewUrl": "https://edge.gift/gift-assets/snow_globe/sha256-24e8cd4c3dacd293/preview.webp?v=sha256-24e8cd4c3dacd293",
      "animationUrl": "https://edge.gift/gift-assets/snow_globe/sha256-24e8cd4c3dacd293/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-snow_mittens",
    "telegramGiftId": "snow_mittens",
    "giftName": "snow_mittens",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "snow_mittens",
      "previewUrl": "https://edge.gift/gift-assets/snow_mittens/sha256-8c1bd2a1b6c9bccd/preview.webp?v=sha256-8c1bd2a1b6c9bccd",
      "animationUrl": "https://edge.gift/gift-assets/snow_mittens/sha256-8c1bd2a1b6c9bccd/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-spiced_wine",
    "telegramGiftId": "spiced_wine",
    "giftName": "spiced_wine",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "spiced_wine",
      "previewUrl": "https://edge.gift/gift-assets/spiced_wine/sha256-19980f2b890149e9/preview.webp?v=sha256-19980f2b890149e9",
      "animationUrl": "https://edge.gift/gift-assets/spiced_wine/sha256-19980f2b890149e9/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-spring_basket",
    "telegramGiftId": "spring_basket",
    "giftName": "spring_basket",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "spring_basket",
      "previewUrl": "https://edge.gift/gift-assets/spring_basket/sha256-ff6d16ef2d101ea8/preview.webp?v=sha256-ff6d16ef2d101ea8",
      "animationUrl": "https://edge.gift/gift-assets/spring_basket/sha256-ff6d16ef2d101ea8/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-spy_agaric",
    "telegramGiftId": "spy_agaric",
    "giftName": "spy_agaric",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "spy_agaric",
      "previewUrl": "https://edge.gift/gift-assets/spy_agaric/sha256-c02391b3b71eebc6/preview.webp?v=sha256-c02391b3b71eebc6",
      "animationUrl": "https://edge.gift/gift-assets/spy_agaric/sha256-c02391b3b71eebc6/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-star",
    "telegramGiftId": "star",
    "giftName": "star",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "star",
      "previewUrl": "https://edge.gift/gift-assets/star/sha256-9f86c0e5bcff27bb/preview.webp?v=sha256-9f86c0e5bcff27bb",
      "animationUrl": "https://edge.gift/gift-assets/star/sha256-9f86c0e5bcff27bb/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-star_notepad",
    "telegramGiftId": "star_notepad",
    "giftName": "star_notepad",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "star_notepad",
      "previewUrl": "https://edge.gift/gift-assets/star_notepad/sha256-46a0c05da2d0a5e4/preview.webp?v=sha256-46a0c05da2d0a5e4",
      "animationUrl": "https://edge.gift/gift-assets/star_notepad/sha256-46a0c05da2d0a5e4/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-stellar_rocket",
    "telegramGiftId": "stellar_rocket",
    "giftName": "stellar_rocket",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "stellar_rocket",
      "previewUrl": "https://edge.gift/gift-assets/stellar_rocket/sha256-1110674e96b4e74f/preview.webp?v=sha256-1110674e96b4e74f",
      "animationUrl": "https://edge.gift/gift-assets/stellar_rocket/sha256-1110674e96b4e74f/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-surge_board",
    "telegramGiftId": "surge_board",
    "giftName": "Surge Board",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "surge_board",
      "previewUrl": "https://edge.gift/gift-assets/surge_board/changes-9cc9d446e6fb-abc7bd26/preview.png?v=changes-9cc9d446e6fb-abc7bd26",
      "animationUrl": "https://edge.gift/gift-assets/surge_board/changes-9cc9d446e6fb-abc7bd26/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-swag_bag",
    "telegramGiftId": "swag_bag",
    "giftName": "swag_bag",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "swag_bag",
      "previewUrl": "https://edge.gift/gift-assets/swag_bag/sha256-5975769fc20e141f/preview.webp?v=sha256-5975769fc20e141f",
      "animationUrl": "https://edge.gift/gift-assets/swag_bag/sha256-5975769fc20e141f/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-swiss_watch",
    "telegramGiftId": "swiss_watch",
    "giftName": "swiss_watch",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "swiss_watch",
      "previewUrl": "https://edge.gift/gift-assets/swiss_watch/sha256-9c8703c333a31923/preview.webp?v=sha256-9c8703c333a31923",
      "animationUrl": "https://edge.gift/gift-assets/swiss_watch/sha256-9c8703c333a31923/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-tama_gadget",
    "telegramGiftId": "tama_gadget",
    "giftName": "tama_gadget",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "tama_gadget",
      "previewUrl": "https://edge.gift/gift-assets/tama_gadget/sha256-82372c19106767f7/preview.webp?v=sha256-82372c19106767f7",
      "animationUrl": "https://edge.gift/gift-assets/tama_gadget/sha256-82372c19106767f7/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-teddy_bear",
    "telegramGiftId": "teddy_bear",
    "giftName": "teddy_bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "teddy_bear",
      "previewUrl": "https://edge.gift/gift-assets/teddy_bear/sha256-d8851b1716c65950/preview.webp?v=sha256-d8851b1716c65950",
      "animationUrl": "https://edge.gift/gift-assets/teddy_bear/sha256-d8851b1716c65950/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-timeless_book",
    "telegramGiftId": "timeless_book",
    "giftName": "timeless_book",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "timeless_book",
      "previewUrl": "https://edge.gift/gift-assets/timeless_book/sha256-ae9c0e252f97907d/preview.png?v=sha256-ae9c0e252f97907d",
      "animationUrl": "https://edge.gift/gift-assets/timeless_book/sha256-ae9c0e252f97907d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-top_hat",
    "telegramGiftId": "top_hat",
    "giftName": "top_hat",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "top_hat",
      "previewUrl": "https://edge.gift/gift-assets/top_hat/sha256-ebe031fe8edb2149/preview.webp?v=sha256-ebe031fe8edb2149",
      "animationUrl": "https://edge.gift/gift-assets/top_hat/sha256-ebe031fe8edb2149/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-toy_bear",
    "telegramGiftId": "toy_bear",
    "giftName": "toy_bear",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "toy_bear",
      "previewUrl": "https://edge.gift/gift-assets/toy_bear/sha256-542cab88376feb24/preview.webp?v=sha256-542cab88376feb24",
      "animationUrl": "https://edge.gift/gift-assets/toy_bear/sha256-542cab88376feb24/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-trapped_heart",
    "telegramGiftId": "trapped_heart",
    "giftName": "trapped_heart",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "trapped_heart",
      "previewUrl": "https://edge.gift/gift-assets/trapped_heart/sha256-00357da01761f08a/preview.webp?v=sha256-00357da01761f08a",
      "animationUrl": "https://edge.gift/gift-assets/trapped_heart/sha256-00357da01761f08a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-ufc_strike",
    "telegramGiftId": "ufc_strike",
    "giftName": "ufc_strike",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "ufc_strike",
      "previewUrl": "https://edge.gift/gift-assets/ufc_strike/sha256-8da4d80bc647c896/preview.png?v=sha256-8da4d80bc647c896",
      "animationUrl": "https://edge.gift/gift-assets/ufc_strike/sha256-8da4d80bc647c896/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-valentine_box",
    "telegramGiftId": "valentine_box",
    "giftName": "valentine_box",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "valentine_box",
      "previewUrl": "https://edge.gift/gift-assets/valentine_box/sha256-703185ab50431c6e/preview.webp?v=sha256-703185ab50431c6e",
      "animationUrl": "https://edge.gift/gift-assets/valentine_box/sha256-703185ab50431c6e/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-vice_cream",
    "telegramGiftId": "vice_cream",
    "giftName": "vice_cream",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "vice_cream",
      "previewUrl": "https://edge.gift/gift-assets/vice_cream/sha256-d18c499c61f4b3ac/preview.png?v=sha256-d18c499c61f4b3ac",
      "animationUrl": "https://edge.gift/gift-assets/vice_cream/sha256-d18c499c61f4b3ac/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-victory_medal",
    "telegramGiftId": "victory_medal",
    "giftName": "victory_medal",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "victory_medal",
      "previewUrl": "https://edge.gift/gift-assets/victory_medal/sha256-19c037835213b58e/preview.png?v=sha256-19c037835213b58e",
      "animationUrl": "https://edge.gift/gift-assets/victory_medal/sha256-19c037835213b58e/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-vintage_cigar",
    "telegramGiftId": "vintage_cigar",
    "giftName": "vintage_cigar",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "vintage_cigar",
      "previewUrl": "https://edge.gift/gift-assets/vintage_cigar/sha256-b6a7f92f1312dd9d/preview.webp?v=sha256-b6a7f92f1312dd9d",
      "animationUrl": "https://edge.gift/gift-assets/vintage_cigar/sha256-b6a7f92f1312dd9d/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-voodoo_doll",
    "telegramGiftId": "voodoo_doll",
    "giftName": "voodoo_doll",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "voodoo_doll",
      "previewUrl": "https://edge.gift/gift-assets/voodoo_doll/sha256-3ebb54330e2acc53/preview.webp?v=sha256-3ebb54330e2acc53",
      "animationUrl": "https://edge.gift/gift-assets/voodoo_doll/sha256-3ebb54330e2acc53/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-westside_sign",
    "telegramGiftId": "westside_sign",
    "giftName": "westside_sign",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "westside_sign",
      "previewUrl": "https://edge.gift/gift-assets/westside_sign/sha256-70fe9df21893c8f4/preview.webp?v=sha256-70fe9df21893c8f4",
      "animationUrl": "https://edge.gift/gift-assets/westside_sign/sha256-70fe9df21893c8f4/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-whip_cupcake",
    "telegramGiftId": "whip_cupcake",
    "giftName": "whip_cupcake",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "whip_cupcake",
      "previewUrl": "https://edge.gift/gift-assets/whip_cupcake/sha256-f35a241c57efd21a/preview.webp?v=sha256-f35a241c57efd21a",
      "animationUrl": "https://edge.gift/gift-assets/whip_cupcake/sha256-f35a241c57efd21a/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-winter_wreath",
    "telegramGiftId": "winter_wreath",
    "giftName": "winter_wreath",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "winter_wreath",
      "previewUrl": "https://edge.gift/gift-assets/winter_wreath/sha256-84cf587163bc5073/preview.webp?v=sha256-84cf587163bc5073",
      "animationUrl": "https://edge.gift/gift-assets/winter_wreath/sha256-84cf587163bc5073/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-witch_hat",
    "telegramGiftId": "witch_hat",
    "giftName": "witch_hat",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "witch_hat",
      "previewUrl": "https://edge.gift/gift-assets/witch_hat/sha256-63e38ed02e1dd1b2/preview.webp?v=sha256-63e38ed02e1dd1b2",
      "animationUrl": "https://edge.gift/gift-assets/witch_hat/sha256-63e38ed02e1dd1b2/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  },
  {
    "itemKey": "gift-xmas_stocking",
    "telegramGiftId": "xmas_stocking",
    "giftName": "xmas_stocking",
    "rewardKind": "telegram_gift",
    "modelName": None,
    "media": {
      "assetKey": "xmas_stocking",
      "previewUrl": "https://edge.gift/gift-assets/xmas_stocking/sha256-832a4463329691a0/preview.webp?v=sha256-832a4463329691a0",
      "animationUrl": "https://edge.gift/gift-assets/xmas_stocking/sha256-832a4463329691a0/animation.lottie",
      "previewMimeType": "image/png",
      "animationMimeType": "application/dotlottie+zip"
    },
    "priceGold": 100,
    "priceSilver": 100,
    "rarityId": "legendary"
  }
]

MOCK_USER = {
    "id": 123456789,
    "telegramId": 123456789,
    "username": "player",
    "firstName": "Игрок",
    "lastName": "",
    "languageCode": "ru",
    "languagePref": "ru",
    "edgeBalance": 100000,
    "silverBalance": 500000,
    "avatarUrl": "/favicon.ico",
    "isPremium": True,
    "role": "user",
    "createdAt": "2026-01-01T00:00:00.000Z",
    "economyMode": "full",
    "realEconomyAllowed": True,
    "inventory": ALL_GIFTS[:50]
}

CATALOG_PATH = os.path.join(DIRECTORY, "catalog.json")
CATALOG_DATA = b"{}"
if os.path.exists(CATALOG_PATH):
    with open(CATALOG_PATH, "rb") as f:
        CATALOG_DATA = f.read()

def get_user_balance():
    return MOCK_USER["edgeBalance"], MOCK_USER["silverBalance"]

def update_user_balance(gold, silver):
    MOCK_USER["edgeBalance"] = gold
    MOCK_USER["silverBalance"] = silver

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

mines_engine = MinesEngine(get_user_balance, update_user_balance)

class StandaloneHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def send_json(self, data, status=200):
        body = json.dumps(data).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS, PUT, DELETE")
        self.send_header("Access-Control-Allow-Headers", "*")
        self.end_headers()

    def do_POST(self):
        content_len = int(self.headers.get("Content-Length", 0))
        body_data = {}
        if content_len > 0:
            try:
                body_data = json.loads(self.rfile.read(content_len).decode("utf-8"))
            except Exception:
                body_data = {}

        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path
        
        if path == "/api/mines/start":
            return self.send_json(mines_engine.start_game(body_data))
        if path == "/api/mines/reveal":
            cell_idx = int(body_data.get("cellIndex", 0))
            return self.send_json(mines_engine.reveal_cell(cell_idx))
        if path == "/api/mines/cashout":
            return self.send_json(mines_engine.cashout())
        if path == "/api/mines/winner/sell":
            return self.send_json({"ok": True})

        if path.startswith("/api/rocket/ws-token"):
            host_val = self.headers.get("Host", "localhost:8080")
            return self.send_json({"ok": True, "token": "mock-ws-token-123", "wsUrl": f"ws://{host_val}/ws"})

        if path.startswith("/api/cases/open"):
            win_item = ALL_GIFTS[0]
            return self.send_json({
                "ok": True,
                "status": "settled",
                "openingId": "open-12345",
                "reward": win_item,
                "rewardValue": {"amount": 100, "currency": "gold"},
                "balancesAfter": {"gold": MOCK_USER["edgeBalance"], "silver": MOCK_USER["silverBalance"]},
                "openedAt": datetime.datetime.now(datetime.timezone.utc).isoformat()
            })

        if path.startswith("/api/users/register"):
            return self.send_json({"success": True, "user": MOCK_USER})
        
        if path.startswith("/api/game-sessions"):
            return self.send_json({
                "success": True,
                "session": {
                    "id": "session-12345",
                    "gameId": "mines",
                    "status": "active"
                }
            })
            
        if path.startswith("/api/"):
            return self.send_json({"success": True, "ok": True, "data": None})
            
        self.send_json({"success": True})

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/api/mines/state":
            return self.send_json(mines_engine.get_state())

        if path.startswith("/api/mines/limits"):
            query = urllib.parse.parse_qs(parsed.query)
            bombs = query.get("bombs", [3])[0]
            return self.send_json(mines_engine.get_limits(bombs))

        if path == "/api/mines/history":
            return self.send_json({"ok": True, "history": []})

        if path == "/api/mines/recent-wins":
            return self.send_json({"ok": True, "recentWins": []})

        if path == "/api/mines/inventory":
            return self.send_json({"ok": True, "items": ALL_GIFTS[:10]})

        if path == "/api/rocket/config":
            return self.send_json({
                "timings": {"waitingDuration": 9000, "crashedDisplayDuration": 2800, "settlingDuration": 2000, "resultsDuration": 2800, "multiplierCorrectionInterval": 200, "multiplierDoublingInterval": 3000},
                "growth": {"tickInterval": 200, "baseRate": 0.01, "acceleration": 1.08, "maxStep": 25},
                "limits": {"minBet": {"gold": 10, "silver": 10}, "maxBet": {"gold": 10000, "silver": 10000}, "minAutoCashout": 1.01, "maxAutoCashout": 250},
                "flags": {"allowGiftBets": True, "allowSilverCurrency": True, "showGiftAnimations": True, "giftAnimationsSelfOnly": False},
                "defaults": {"previewBetAmount": 200}
            })

        if path == "/api/rocket/prizes":
            return self.send_json({"prizes": ALL_GIFTS[:20]})

        if path.startswith("/api/rocket/history"):
            return self.send_json({"rounds": []})

        if path == "/api/rocket/inventory" or path == "/api/rocket/balance":
            return self.send_json({"gold": MOCK_USER["edgeBalance"], "silver": MOCK_USER["silverBalance"], "items": ALL_GIFTS[:20]})

        if path.startswith("/api/cases/state") or path == "/api/cases/catalog":
            case_items = ALL_GIFTS[:30]
            item_keys = [it["itemKey"] for it in case_items]
            return self.send_json({
                "catalogVersion": 1,
                "policyVersion": 1,
                "pricingVersion": "native-gold-silver-parity.v1",
                "balances": {"gold": MOCK_USER["edgeBalance"], "silver": MOCK_USER["silverBalance"]},
                "cases": [
                    {
                        "caseKey": "official-nft-case",
                        "name": "NFT TG Gifts Case",
                        "displayOrder": 1,
                        "coverImageUrl": case_items[0]["media"]["previewUrl"],
                        "itemCount": len(case_items),
                        "items": case_items,
                        "wager": {
                            "defaultOptionId": "wager-1",
                            "options": [{
                                "optionId": "wager-1",
                                "cost": {"gold": 100, "silver": 100},
                                "itemKeys": item_keys,
                                "itemKeysByCurrency": {
                                    "gold": item_keys,
                                    "silver": item_keys
                                }
                            }]
                        },
                        "canonicalSnapshotHash": "snapshot-hash-12345",
                        "availability": {"gold": "available", "silver": "available"}
                    }
                ],
                "serverTime": datetime.datetime.now(datetime.timezone.utc).isoformat()
            })

        if path.startswith("/api/upgrade/state"):
            return self.send_json({
                "status": "ready",
                "user": MOCK_USER,
                "balances": {"gold": MOCK_USER["edgeBalance"], "silver": MOCK_USER["silverBalance"]},
                "inventory": ALL_GIFTS[:30],
                "items": ALL_GIFTS[:30]
            })

        if path == "/api/gift-assets/manifest":
            return self.send_json(manifest_data)

        if path == "/api/games/catalog":
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(CATALOG_DATA)))
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(CATALOG_DATA)
            return

        if path == "/api/cases/health/ready":
            return self.send_json({"ready": True})

        if path == "/api/stats/online":
            return self.send_json({"online": 1284, "playing": 491})

        if path == "/api/giveaways/rewards/pending":
            return self.send_json({"success": True, "rewards": []})

        if path == "/api/games/recent-wins":
            return self.send_json({"success": True, "wins": [], "todayTotal": 14820})

        if path.startswith("/api/users/register") or path == "/api/users/me" or path == "/api/profile" or path == "/api/user/profile":
            return self.send_json({"success": True, "ok": True, "user": MOCK_USER, "profile": MOCK_USER, "inventory": ALL_GIFTS[:50]})

        if path.startswith("/api/daily-case"):
            return self.send_json({"available": True, "streak": 5})

        if path.startswith("/api/security/reward-challenge"):
            return self.send_json({"enabled": False, "required": False})

        if path.startswith("/api/"):
            return self.send_json({"success": True, "ok": True, "status": "ready", "data": {}})

        for game_name in ["mines", "rocket", "roulette", "cases", "upgrade", "pvp-bombs", "minedrop", "stack-drop", "falling-pickaxe", "pot-battle", "edge-ice"]:
            prefix = f"/{game_name}-app"
            if path == prefix or path == f"{prefix}/":
                app_file = os.path.join(DIRECTORY, f"{game_name}-app", "index.html")
                if not os.path.exists(app_file):
                    app_file = os.path.join(DIRECTORY, "mines-app", "index.html")
                if os.path.exists(app_file):
                    with open(app_file, "rb") as f:
                        body = f.read()
                    self.send_response(200)
                    self.send_header("Content-Type", "text/html; charset=utf-8")
                    self.send_header("Content-Length", str(len(body)))
                    self.send_header("Access-Control-Allow-Origin", "*")
                    self.end_headers()
                    self.wfile.write(body)
                    return

        translated = self.translate_path(self.path)
        if not os.path.exists(translated):
            base, ext = os.path.splitext(translated)
            if not ext or ext in [".html"]:
                self.path = "/index.html"

        super().do_GET()

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        super().end_headers()

def get_lan_ips():
    ips = []
    try:
        import socket
        hostname = socket.gethostname()
        for ip in socket.gethostbyname_ex(hostname)[2]:
            if not ip.startswith("127."):
                ips.append(ip)
    except Exception:
        pass
    return ips

if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    with socketserver.ThreadingTCPServer(("", PORT), StandaloneHandler) as httpd:
        lan_ips = get_lan_ips()
        print("=" * 60)
        print("SERVER RUNNING AND READY (STANDALONE / NO TELEGRAM):")
        print(f"   PC:     http://localhost:{PORT}")
        for ip in lan_ips:
            if ip.startswith("192.168.") or ip.startswith("10."):
                print(f"   PHONE:  http://{ip}:{PORT}")
            elif ip.startswith("26."):
                print(f"   VPN:    http://{ip}:{PORT}")
        print("=" * 60)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
