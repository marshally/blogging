# Image ledger

## Conference QR code and iPhone wallpaper

Created on 2026-10-13 for Marshall's conference sharing. The QR code contains exactly `https://vibeengineeringprimer.com/`. These are original project graphics, generated deterministically with Python `qrcode` 8.2 and Pillow 12.3.0. No stock images or third-party artwork are included.

| Asset | Repository master | Published copy | Dimensions |
|---|---|---|---|
| Standalone QR code | [PNG](../images/vibe-primer-qr.png) | [qr.png](https://vibeengineeringprimer.com/qr.png) | 943 × 943 pixels |
| Vector QR master | [SVG](../images/vibe-primer-qr.svg) | [qr.svg](https://vibeengineeringprimer.com/qr.svg) | 41 × 41 modules including the border |
| Conference lock-screen wallpaper | [PNG](../images/vibe-primer-wallpaper.png) | [wallpaper.png](https://vibeengineeringprimer.com/wallpaper.png) | 1290 × 2796 pixels |

- **What it shows:** A black QR code on white. The wallpaper adds the working book title, Marshall's name, the destination domain, and “Scan for book updates” on the landing page's dark green background. The top and bottom leave room for phone controls.
- **Source page and destination:** [The Vibe Engineer’s Primer landing page](https://vibeengineeringprimer.com/).
- **Creator/source:** Original project graphics generated for Marshall Yount. Georgia and Arial system fonts are rasterized into the wallpaper.
- **License:** Own project artwork; no third-party image license applies.
- **Encoding:** QR version 4, Q error correction, 23 pixels per module, four-module white quiet zone. The SVG includes a white background.
- **Device reference:** The wallpaper dimensions match Apple's [iPhone 15 Pro Max display specifications](https://support.apple.com/en-us/111828). Actual wallpaper cropping and notifications depend on the phone's settings.
- **Verification:** Visually inspected at phone display size. ZXing-C++ 3.1.1 decoded the exact URL from the QR PNG, the full wallpaper, and 390-pixel-wide and 320-pixel-wide wallpaper previews. A physical scan of the configured lock screen remains a user check.
