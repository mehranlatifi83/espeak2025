# eSpeak NG 2025.2 for NVDA

An NVDA add-on that replaces NVDA's built-in eSpeak NG with the eSpeak NG version that shipped with NVDA 2025.2.

افزونه‌ای برای NVDA که eSpeak داخلی NVDA را با نسخه‌ی eSpeak NG که در NVDA 2025.2 بود جایگزین می‌کند.

## English

- The synthesizer keeps the same name as the built-in one (`espeak`), so your voice, rate, variant and other eSpeak settings, and your eSpeak voice dictionaries, keep working as before.
  It shows in the synthesizer list as "eSpeak NG (2025.2)".
- NVDA itself is not modified. It stays the official, signed NVDA, so it can still read applications running as administrator.
- Removing or disabling the add-on brings back NVDA's own eSpeak NG after restarting NVDA.
- The synth driver is a copy of NVDA 2026.3.1's own eSpeak driver, only changed to load eSpeak from the add-on's folder.

Requires NVDA 2026.3 or later (64-bit).

## فارسی

- اسم سنتسایزر همان `espeak` خود NVDA است؛ پس صدا، سرعت، تغییر صدا (variant)، بقیه‌ی تنظیمات eSpeak و دیکشنری‌های صدای eSpeak شما مثل قبل کار می‌کنند.
  در فهرست سنتسایزرها با نام «eSpeak NG (2025.2)» دیده می‌شود.
- هیچ فایلی از خود NVDA تغییر نمی‌کند و NVDA همان نسخه‌ی رسمی و امضاشده می‌ماند؛ برای همین برنامه‌هایی که با دسترسی ادمین اجرا شده‌اند هم خوانده می‌شوند.
- با حذف یا غیرفعال کردن افزونه و ری‌استارت NVDA، eSpeak خود NVDA برمی‌گردد.

## Source

- eSpeak NG: [espeak-ng/espeak-ng@e93d3a97](https://github.com/espeak-ng/espeak-ng/tree/e93d3a97ee9237f7e170cc8870f44c14de9032a9), the commit used by NVDA 2025.2.
- Built with NVDA 2026.3.1's build scripts: [mehranlatifi83/nvda, branch try-2026.3.1-espeak2025.2](https://github.com/mehranlatifi83/nvda/tree/try-2026.3.1-espeak2025.2).

## Build

```
python build.py
```

## License

The synth driver is based on NVDA's code (GNU GPL version 2 or later). eSpeak NG is licensed under the GNU GPL version 3 or later. The add-on as a whole is distributed under the GNU GPL version 3 or later.
