from tkinter import Tk, filedialog

def parse_quiz_file():
    questionnaires = {}

    # Create hidden Tkinter window
    root = Tk()
    root.withdraw()

    # Open file dialog
    file_path = filedialog.askopenfilename(
        title="Select Quiz File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not file_path:
        print("No file selected.")
        return {}

    # Read file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split into question blocks
    blocks = content.strip().split('-')

    for block in blocks:
        block = block.strip()
        if not block:
            continue

        parts = block.split('\n\n')

        if len(parts) != 6:
            # print("Skipping malformed block:\n", block)
            continue

        try:
            # Extract question
            q_num, question = parts[0].split('.', 1)

            # Extract choices
            a_key, a_val = parts[1].split('.', 1)
            b_key, b_val = parts[2].split('.', 1)
            c_key, c_val = parts[3].split('.', 1)
            d_key, d_val = parts[4].split('.', 1)

            # Extract correct answer (case-insensitive)
            correct_key, correct_val = parts[5].split(':', 1)

            questionnaires[int(q_num.strip())] = {
                question.strip(): {
                    a_key.strip(): a_val.strip(),
                    b_key.strip(): b_val.strip(),
                    c_key.strip(): c_val.strip(),
                    d_key.strip(): d_val.strip(),
                    "Correct": correct_val.strip().upper()
                }
            }

        except Exception as e:
            print("Error parsing block:\n", block)
            print("Error:", e)

    return questionnaires