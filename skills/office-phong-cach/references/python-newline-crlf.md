---
name: python-sua-file-newline
description: "Sửa file trong repo bằng Python mà quên newline='' là đổi CRLF sang LF cả file, git báo toàn bộ file thay đổi"
---

> Nguồn: ghi nhớ `python-sua-file-newline`, cập nhật 2026-09-03. Chép tự động bằng `scripts/sync.py` — sửa ở ghi nhớ gốc rồi chạy lại.

Khi sửa file nguồn bằng script Python (`io.open(...).read()` rồi ghi lại), phải mở
**cả lúc đọc lẫn lúc ghi** với `newline=''`. Thiếu nó lúc đọc thì Python dịch `\r\n`
thành `\n`, ghi ra là **cả file chuyển sang LF** — `git diff` báo thay đổi từng dòng
của file dù chỉ sửa một câu.

Cùng lý do: chuỗi nhiều dòng viết trong script dùng `\n`, còn file dùng `\r\n`, nên
`assert a in s` trượt. Chuẩn hoá trước khi so:

```python
s = io.open(p, encoding='utf-8-sig', newline='').read()
nl = '\r\n' if '\r\n' in s else '\n'
def n(t): return t.replace('\r\n', '\n').replace('\n', nl)
```

**Why:** repo MP_MES có `.gitattributes` bắt `* text=auto eol=crlf`, nhưng working
tree đang lẫn lộn — vài file (`MayInService.cs`, `RibbonBuilder.cs`) vốn đã là LF từ
các phiên trước. Nên không thể giả định file nào cũng CRLF.

**How to apply:** dò `nl` từ chính file đang sửa như trên. Sửa xong kiểm bằng
`python -c "raw=open(f,'rb').read(); print(raw.count(b'\r\n'))"`, hoặc `git diff --stat`
— một sửa đổi nhỏ mà diff ra hàng trăm dòng là dấu hiệu đã nuốt mất CRLF. Liên quan:
[ps51-utf8-script-encoding](ps51-utf8-tieng-viet.md), *heredoc-nuot-backslash-n*.
