# Changelog

## [0.1.2] - 2026-11-18

### Fixed

- Request sign-in again when account authorization expires or is rejected.
- Keep temporary connection failures recoverable without requesting sign-in.
- Show translated errors when device commands fail.
- Remove account identifiers from downloaded diagnostics.
- Replace the inactive token repair prompt with Home Assistant reauthentication.
- Correct release metadata and logging configuration.

## [0.1.1] - 2026-09-15

### Added

- Initial HACS distribution for Gree Plus cloud air conditioners.
- Support for power, HVAC mode, temperature, fan speed, and manual refresh.
- Browser verification fallback when automated sign-in requires a CAPTCHA.
- User guides in English, German, Spanish, French, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Traditional Chinese.

### Fixed

- Prevented a previous sign-in session from affecting a new credential attempt.
- Clarified the browser verification steps, including the expected localhost redirect.
