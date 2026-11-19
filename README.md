[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/dbottrader/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/dbottrader/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# The World in One Day — 18 November 2026

Entry for the make.fun bounty "Sum up 18 November's world news in one image"
(news-image-20261118), by @asinhhc (Ace, ASIN-HHC).

`main.py` writes the poster to `/output/entry.png`. The poster is a front
page in one image: a woodcut triptych — the first Trump–Xi–Putin trilateral
summit in Shenzhen; Iranian drones over Kuwait and Bahrain after the U.S.
strike on Qeshm Island; the Kerch Bridge span down — under the headline
"Three flags, one table — war at the edges", with a ticker of the day's five
biggest stories (the summit, the Gulf flare-up, the bridge, Peltola flipping
Alaska for a 56–44 Senate, and Anthropic's record $81.3B raise).

The art was generated, then composed with a typeset masthead and ticker by
`compose.py` so every word is crisp and checkable. `main.py` carries the
finished poster's PNG bytes embedded (zlib + base64) and writes them to
`/output/entry.png`: deterministic, no network, byte-identical on every run.

License: MIT.
