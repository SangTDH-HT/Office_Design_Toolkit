---
name: csc-can-bom-cho-tieng-viet
description: "File .cs UTF-8 không BOM bị csc đọc theo codepage hệ thống, làm hỏng mọi chuỗi tiếng Việt mà build vẫn thành công"
---

> Nguồn: ghi nhớ `csc-can-bom-cho-tieng-viet`. Đã lược phần riêng dự án; bản này sửa trực tiếp trong repo.

Trình biên dịch C# của .NET Framework (`csc`) đọc file nguồn **không có BOM** theo
codepage ANSI của hệ thống, không phải UTF-8. Chuỗi tiếng Việt trong code sẽ ra chữ rác
mà **build vẫn thành công** — chỉ lộ ra lúc chạy.

Hai lớp phòng cùng lúc:
- Thêm BOM (`EF BB BF`) vào mọi file `.cs` và `.xaml`
- Đặt `<CodePage>65001</CodePage>` trong `.csproj`

Công cụ ghi file (heredoc bash, script python) mặc định **không** thêm BOM, nên phải tự
thêm sau khi tạo file. Kiểm tra: `head -c3 file.cs | od -An -tx1` phải ra `ef bb bf`.

Công cụ khác xuất nguồn **có BOM** cũng vậy: sửa bằng python/heredoc rồi ghi lại không BOM là
chú thích tiếng Việt thành `ÄIá»€U KHIá»‚N` — biên dịch vẫn 0 lỗi. Ghi bằng `encoding='utf-8-sig'`.

Cùng họ với [ps51-utf8-script-encoding](ps51-utf8-tieng-viet.md).
