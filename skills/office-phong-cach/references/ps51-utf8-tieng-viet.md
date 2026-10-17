---
name: ps51-utf8-script-encoding
description: "PowerShell 5.1 reads UTF-8-no-BOM .ps1 files as ANSI, so Vietnamese literals in scripts cause parser errors — keep scripts ASCII and load text from a JSON/txt file"
---

> Nguồn: ghi nhớ `ps51-utf8-script-encoding`, cập nhật 2026-10-12. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Windows PowerShell 5.1 (the only edition here) decodes `.ps1` files written by the Write tool (UTF-8 without BOM) as the ANSI codepage. Any Vietnamese literal inside the script turns into mojibake and usually breaks the parser ("Unexpected token", "string is missing the terminator").

**Why:** hit three times in one session while driving Word/Excel via COM; each failure costs a round trip and can leave a half-applied document edit behind.

**How to apply:** MP MES test scripts (tools\kiem-thu-*) DO keep Vietnamese — they are saved WITH BOM. After writing a .ps1 with the Write tool, re-save it: `[IO.File]::WriteAllText($p, [IO.File]::ReadAllText($p), (New-Object Text.UTF8Encoding($true)))`, then parse-check before running: `[System.Management.Automation.Language.Parser]::ParseFile($p,[ref]$t,[ref]$e)` (hit again 13/10/2026 with thu-thoi-gian.ps1 — 100+ bogus parse errors, all from the missing BOM). Otherwise keep `.ps1` bodies pure ASCII. Put Vietnamese strings in a side file and load them explicitly — `Get-Content data.json -Raw -Encoding UTF8 | ConvertFrom-Json` or `[IO.File]::ReadAllLines($p,[Text.Encoding]::UTF8)`. For matching existing Vietnamese text, match an ASCII-only fragment (`-match 'MINH, N'`). Write output back with `[IO.File]::WriteAllLines($p,$out,[Text.Encoding]::UTF8)` and read it with the Read tool, since console output is mangled too. See *word-com-automation*.
