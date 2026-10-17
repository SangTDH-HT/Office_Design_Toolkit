---
name: sendkeys-bi-bo-go-tieng-viet-an
description: "SendKeys gõ chữ Latin bị Unikey/EVKey biến thành chữ có dấu — dán từ clipboard thay vì gõ"
---

> Nguồn: ghi nhớ `sendkeys-bi-bo-go-tieng-viet-an`, cập nhật 2026-08-24. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Máy anh Sáng luôn bật bộ gõ tiếng Việt kiểu telex. `[System.Windows.Forms.SendKeys]::SendWait`
đi qua bàn phím thật nên bộ gõ ăn vào giữa:

* `MP_MES` → `MP_MÉ` (telex hiểu `e` + `s` = `é`)
* bất kỳ chuỗi nào có `as ax af ar aj`, `es ex…`, `oo`, `dd`… đều bị đổi

Hộp thoại chỉ báo "Path does not exist", nhìn thoáng qua không thấy sai ở đâu.

**How to apply:** trong script tự động hoá giao diện, đường dẫn và mọi chuỗi chữ
Latin phải **dán** chứ đừng gõ:

```powershell
Set-Clipboard -Value "C:\MinhPhuc\MP_MES\tools\ra.pdf"
Start-Sleep -Milliseconds 300
[System.Windows.Forms.SendKeys]::SendWait("^a")
[System.Windows.Forms.SendKeys]::SendWait("^v")
```

Chuỗi chỉ có chữ số (ngày `21/08/2026`) thì gõ thẳng vẫn an toàn.
Xem *mp-mes-vong-nghiem-thu*, [ps51-utf8-script-encoding](ps51-utf8-tieng-viet.md).
