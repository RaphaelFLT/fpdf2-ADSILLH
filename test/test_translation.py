from fpdf import FPDF
from fpdf.drawing_primitives import Transform


def create_translation_demo():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=10)

    # --- Demo Parameters ---
    x_rect, y_rect = 10, 30  # Original coordinates
    w_rect, h_rect = 40, 20  # Size of the rectangle
    dx, dy = 60, 20  # Translation Vector (Shift distance)

    # 1. Reference Drawing (Black)
    # This represents the object drawn at its original coordinates.
    pdf.set_draw_color(0, 0, 0)  # Black
    pdf.set_line_width(0.3)
    pdf.text(x_rect, y_rect - 2, "1. Original Object")
    pdf.rect(x_rect, y_rect, w_rect, h_rect)

    # 2. Transformed Drawing (Red)
    # We apply a translation matrix to the graphics context.
    pdf.set_draw_color(220, 50, 50)  # Red
    pdf.set_text_color(220, 50, 50)

    # The 'with' block applies the shift (dx, dy)
    with pdf.transform(Transform.translation(x=dx, y=dy)):
        # NOTICE: We use the EXACT SAME coordinates (x_rect, y_rect).
        # The context manager handles the displacement on the page.
        pdf.rect(x_rect, y_rect, w_rect, h_rect)

        # Add centered text inside the red rectangle
        pdf.set_xy(x_rect, y_rect + h_rect / 2 - 2)
        pdf.cell(w_rect, 4, "2. Translated Object", align="C")

    # 3. Visual Explanation (Blue)
    # We draw a line to visualize the translation vector.
    # We calculate absolute coordinates to draw "over" the contexts.
    start_x, start_y = x_rect, y_rect
    end_x, end_y = x_rect + dx, y_rect + dy

    pdf.set_draw_color(0, 100, 200)  # Blue
    pdf.set_text_color(0, 100, 200)

    # A. Dotted Line
    pdf.set_dash_pattern(dash=3, gap=2)
    pdf.line(start_x, start_y, end_x, end_y)
    pdf.set_dash_pattern()  # Reset to solid line

    # B. Target Point (The Anchor)
    pdf.circle(end_x, end_y, 1, style="F")

    # C. Distance Label
    mid_x = (start_x + end_x) / 2
    mid_y = (start_y + end_y) / 2

    # Place text near the middle of the line
    pdf.set_xy(mid_x + 2, mid_y - 6)
    pdf.set_font("Helvetica", "I", 8)
    pdf.cell(30, 5, f"Vector: dx={dx}, dy={dy}")

    # Output
    filename = "translation_demo.pdf"
    pdf.output(filename)
    print(f"Success: {filename} generated.")


if __name__ == "__main__":
    create_translation_demo()
