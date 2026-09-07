function s(){return""}function t(r){if(!r)return null;if(/^https?:\/\//i.test(r)||r.startsWith("/"))return r;const e=s();return e?`${e}${r.startsWith("/")?r:`/${r}`}`:r}export{t as n,s as t};
