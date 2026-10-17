---
name: dat-ten-file
description: "Quy ước Sáng đặt tên thư mục, file tài liệu và bản sao lưu (\"đặt theo phong cách của anh\", 14/09/2026)"
---

> Tổng hợp từ quy ước Sáng dùng khi sắp lại thư mục dự án; đã lược tên dự án.

## Thư mục

- `<số>.<Ten_Thu_Muc>` cho cấp 1 và cấp 3; `<số>.<TEN_VIET_HOA>` cho cấp 2 trong thư mục tài liệu.
- Ví dụ cây tài liệu: `2.Tai_Lieu\{1.TAI_LIEU_LAP_TRINH, 2.NGUYEN_LY_MAY, 3.TAI_LIEU_VAN_HANH, 4.KHAC}` —
  lập trình / nguyên lý / vận hành / khảo sát, tham khảo.
- Thư mục dự án phần mềm (project gốc của công cụ kỹ thuật) giữ tên gốc, không đánh số.
- Không thả file lạ ra gốc dự án — Sáng xoá ngay file quy ước em từng để ở gốc.

## File

- `<số>.<Ten_Tai_Lieu>.pdf`: tiếng Việt **không dấu**, chữ đầu mỗi từ viết hoa, nối `_`.
- **Không** đưa ngày, tên máy, `VI-EN` vào tên file.
- File nguồn (`.html`, `.md`) đặt cùng tên, cạnh `.pdf`.
- Trước khi ghi, `ls` thư mục đích để lấy số thứ tự kế tiếp (đã gặp hai file trùng số).
- Mẫu Excel xuất báo cáo: `File_Mau_Xuat_Bao_Cao_<Loai>_<VI|EN>.xlsx`.

## Bản sao lưu

- Bản cũ trước khi sửa: thêm hậu tố sau đuôi, `….pdf.bak-before-<viec>`, `….xlsx.bak-before-<viec>`.
- Sao lưu cả dự án: một thư mục backup riêng do Sáng chỉ định, tên `<Du_An>_backup_<yyyy-mm-dd>_<HHMM>_<viec>`;
  không rải bản sao cạnh project ở gốc, không để trong scratchpad.

**Why:** file đặt sai chỗ / sai tên thì Sáng phải dời tay rồi nhắc lại; backup rải nhiều chỗ thì lúc cần khôi phục không biết bản nào mới nhất.
