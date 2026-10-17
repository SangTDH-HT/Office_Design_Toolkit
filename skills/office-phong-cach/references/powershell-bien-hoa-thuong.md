---
name: powershell-bien-khong-phan-biet-hoa-thuong
description: "PowerShell không phân biệt hoa thường tên biến: $vai đè $Vai, $mau đè $Mau — bài thử chạy sai im lặng, có lần ghi file 'System.Collections.Hashtable' ra thư mục đang đứng (16/10/2026)"
---

> Nguồn: ghi nhớ `powershell-bien-khong-phan-biet-hoa-thuong`, cập nhật 2026-10-16. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

Hai lần trong ngày 16/10/2026 khi viết bài thử MP MES:
- `foreach ($vai in $Vai)` — vòng lặp gán đè danh sách, từ vòng ngoài thứ hai chỉ còn thử một vai (thu-quyen-them.ps1).
- `$Mau = @{...}` đè `$mau` (đường dẫn file mẫu) → `WriteAllText($mau, …)` ghi ra file tên `System.Collections.Hashtable` ở thư mục đang đứng (thư mục dự án, bin\Debug); bộ nuôi đọc file đó nên mẫu không bao giờ đổi (thu-xep-the.ps1). Đã xoá hai file rác.

Cùng họ: hàm PowerShell in chữ (`''`, `"#####"`) rồi `return $bang` → giá trị trả về thành MẢNG, `$kq['x']` rỗng, `.ContainsKey` nổ trong finally → khâu dọn bỏ dở (thu-chon-don-tp.ps1 lần đầu; đã trả tay + so vân tay với bản COPY_ONLY).

**Why:** lỗi kiểu này không báo gì, bài thử ra HỎNG giả (hoặc ĐẠT giả) và có thể ghi file ra chỗ lạ.
**How to apply:** trong script PowerShell đặt tên biến khác hẳn nhau (không chỉ khác hoa thường — `$CacVai`/`$vai`, `$MauChay`/`$mau`); hàm trả bảng thì in chữ bằng `Write-Host`; trong `finally` kiểm `-is [hashtable]` trước khi gọi phương thức. Liên quan *mp-mes-chay-truoc-chi-trong-bo-nho*, [bash-heredoc-nuot-dau-gach-nguoc](bash-heredoc-gach-nguoc.md).
