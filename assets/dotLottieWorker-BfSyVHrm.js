function w(a) {
	return {
		autoResize: !0,
		freezeOnOffscreen: !0,
		devicePixelRatio: typeof a == "number" && a > 0 ? a : 1,
		useFrameInterpolation: !1
	};
}
function D(a) {
	return a instanceof Error ? a.message : typeof a == "string" ? a : "Unknown dotLottie worker error";
}
function I(a) {
	const n = a;
	return {
		loaded: n.isLoaded === !0,
		ready: n.isReady === !0
	};
}
function M(a = {}) {
	const n = self, P = a.defaultLoop ?? !0, g = a.defaultAutoplay ?? !0, R = a.defaultSpeed ?? 1;
	let t = null, r = null, o = null, s = null, d = null, u = !1, f = null, l = null;
	const k = (e) => {
		const i = {
			type: "ERROR",
			payload: { message: D(e) }
		};
		n.postMessage(i);
	}, p = () => {
		d !== null && (clearTimeout(d), d = null);
	}, b = (e) => {
		if (t) switch (e) {
			case "PLAY":
				t.play();
				break;
			case "PAUSE":
				t.pause();
				break;
			case "STOP":
				t.stop();
				break;
		}
	}, y = (e) => {
		f = e, u && b(e);
	}, S = (e) => {
		if (l = e, !(!u || !t)) {
			try {
				t.setFrame(e);
			} catch {}
			l = null;
		}
	}, m = () => {
		if (!u) {
			if (p(), u = !0, n.postMessage({ type: "LOADED" }), l !== null && t) {
				try {
					t.setFrame(l);
				} catch {}
				l = null;
			}
			f && b(f);
		}
	}, E = () => {
		if (p(), u = !1, f = null, l = null, !!t) {
			r && t.removeEventListener("load", r), o && t.removeEventListener("ready", o), s && t.removeEventListener("loadError", s);
			try {
				t.destroy();
			} catch {}
			t = null, r = null, o = null, s = null;
		}
	}, A = async (e) => {
		E();
		try {
			const { DotLottie: i } = await import("./dist-CKdH30j6.js"), F = typeof e.loop == "boolean" ? e.loop : P, T = typeof e.autoplay == "boolean" ? e.autoplay : g, v = typeof e.speed == "number" && Number.isFinite(e.speed) ? e.speed : R, c = new i({
				canvas: e.canvas,
				data: e.animationData,
				autoplay: T,
				loop: F,
				speed: v,
				useFrameInterpolation: !1,
				renderConfig: w(e.devicePixelRatio)
			});
			o = () => {
				m();
			}, r = () => {
				p(), d = setTimeout(() => {
					m();
				}, 50);
			}, s = (O) => {
				const h = O?.message ?? "Failed to render dotLottie animation";
				k(new Error(h));
			}, c.addEventListener("load", r), c.addEventListener("ready", o), c.addEventListener("loadError", s), t = c;
			const L = I(c);
			L.ready ? queueMicrotask(m) : L.loaded && queueMicrotask(r);
		} catch (i) {
			k(i);
		}
	};
	n.onmessage = (e) => {
		switch (e.data.type) {
			case "INIT":
				A(e.data.payload);
				break;
			case "PLAY":
				y("PLAY");
				break;
			case "PAUSE":
				y("PAUSE");
				break;
			case "STOP":
				y("STOP");
				break;
			case "SET_FRAME":
				S(e.data.payload.frame);
				break;
			case "DESTROY":
				E();
				break;
		}
	};
}
M({
	defaultLoop: !0,
	defaultAutoplay: !1,
	defaultSpeed: 1
});
