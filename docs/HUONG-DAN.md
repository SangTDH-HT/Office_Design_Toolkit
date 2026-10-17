# Hướng dẫn dùng

Gõ bình thường cho Claude; skill tự bật theo câu. Bảng dưới là câu nhờ mẫu và skill sẽ chạy, để biết nên nói thế nào cho trúng.

| Câu nhờ | Skill chạy | Ra gì |
|---|---|---|
| "Căn lề KHBD tuần 7 như hôm bữa" | `office-phong-cach` | `.docx` lề 2-2-3-2, TNR 14, giãn 1,2, bảng như mẫu tuần 5; bản gốc giữ `- ban goc.docx` |
| "Chèn thêm 3 hình vào chương 4 báo cáo, đánh số lại" | `office-phong-cach` | Caption `SEQ HINHVE`, danh mục hình và mục lục cập nhật |
| "Kiểm mấy công thức Excel trong đề ôn này" | `office-phong-cach` | Đáp số do Excel thật tính qua COM |
| "Làm hướng dẫn thao tác cho thợ, xuất PDF" | `tai-lieu-pdf` | Cặp `.html` + `.pdf` khuôn hướng dẫn thao tác, tên `<số>.<Ten_Tai_Lieu>.pdf` đúng số thứ tự |
| "Giải mấy bài này rồi xuất PDF cho anh chép" | `tai-lieu-pdf` | Bài làm TNR 13 đen trắng: Tóm tắt → Bài làm → Vậy |
| "Soạn tài liệu ôn giữa kỳ chương 6–9" | `tai-lieu-pdf` | Khuôn A–G, giải theo phong cách slide, đáp số kiểm sympy |
| "Viết đề xuất đối chiếu dữ liệu cho quản lý" | `tai-lieu-pdf` → `ui-ux-quy-trinh` | `.md` gốc + HTML có đồ thị, artifact riêng tư |
| "Vẽ lưu đồ quy trình bằng draw.io" | `tai-lieu-pdf` | `.drawio` màu tường minh, xuất PNG soát |
| "Đổi màu chữ tiêu đề trong file .ai sang cam" | `adobe-phong-cach` → `illustrator` | JSX qua COM, xuất PNG soát |
| "Xoá nền ảnh sản phẩm này" | `adobe-phong-cach` | Photoshop recipe xoá nền, xem trước |
| "Làm trang dashboard sản lượng cho máy giám sát" | `ui-ux-quy-trinh` | Bảng token + wireframe trước, code sau, soát UX |
| "Màn Máy tính trong MES đang xấu" | `ui-ux-quy-trinh` | Dựng lại theo `Theme.xaml`, khung cửa sổ Windows thường |

## Khi kết quả chưa đúng ý

- Nói thẳng chỗ sai kèm ảnh khoanh — lời chê thành ghi nhớ mới, chạy `python scripts/sync.py` là vào repo.
- Muốn giữ một luật lâu dài: "nhớ luật này" → Claude ghi vào ghi nhớ; thêm tên ghi nhớ vào `scripts/sources.tsv` nếu muốn nó nằm trong skill.
