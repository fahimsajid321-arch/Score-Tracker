import flet as ft
from flet import app as flet_app

PLAYERS = ["Faheem", "Waseem", "Usama", "Waqar", "Wahab"]
TARGET_SCORE = 100


def main(page: ft.Page):
    page.title = "Card Game Score Tracker"
    page.theme_mode = ft.ThemeMode.DARK
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 16

    scores = {p: [] for p in PLAYERS}
    round_number = 1

    # Header
    title = ft.Text(
        "Card Elimination Tracker",
        size=22,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER,
    )
    subtitle = ft.Text(
        f"Target Score: {TARGET_SCORE} (100+ = OUT)",
        size=13,
        color=ft.Colors.GREY_400,
        text_align=ft.TextAlign.CENTER,
    )

    score_cards = {}
    input_fields = {}

    def get_total(player):
        return sum(scores[player])

    def is_out(player):
        return get_total(player) >= TARGET_SCORE

    def close_dialog(dlg):
        page.close(dlg)

    def show_alert(title_text: str, body_text: str):
        dialog = ft.AlertDialog(
            title=ft.Text(title_text),
            content=ft.Text(body_text),
            actions=[
                ft.TextButton("OK", on_click=lambda _: close_dialog(dialog))
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )
        page.open(dialog)

    def check_winner():
        active = [p for p in PLAYERS if not is_out(p)]
        if len(active) == 1:
            show_alert("🎉 Winner!", f"🏆 {active[0]} has won the game!")
        elif len(active) == 0:
            show_alert("Game Over", "All players have been eliminated!")

    # 1. Dashboard Cards
    cards_row = ft.ResponsiveRow(spacing=8, run_spacing=8)
    for player in PLAYERS:
        tot_text = ft.Text("0", size=18, weight=ft.FontWeight.BOLD, color=ft.Colors.GREEN_ACCENT)
        status_text = ft.Text("Active", size=11, color=ft.Colors.GREEN_400)

        card = ft.Container(
            content=ft.Column(
                [
                    ft.Text(player, weight=ft.FontWeight.BOLD, size=13, no_wrap=True),
                    tot_text,
                    status_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=2,
            ),
            padding=8,
            border_radius=8,
            bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
            col={"xs": 6, "sm": 4, "md": 2.4},
        )
        score_cards[player] = {"container": card, "total": tot_text, "status": status_text}
        cards_row.controls.append(card)

    # 2. Input Fields
    inputs_row = ft.ResponsiveRow(spacing=8, run_spacing=8)
    for player in PLAYERS:
        inp = ft.TextField(
            label=player,
            keyboard_type=ft.KeyboardType.NUMBER,
            text_align=ft.TextAlign.CENTER,
            col={"xs": 6, "sm": 4, "md": 2.4},
            dense=True,
        )
        input_fields[player] = inp
        inputs_row.controls.append(inp)

    # 3. Game Log Table
    history_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("R#")),
            *[ft.DataColumn(ft.Text(p)) for p in PLAYERS],
        ],
        rows=[],
        heading_row_height=36,
        data_row_min_height=32,
    )

    def submit_round(e):
        nonlocal round_number
        round_entries = [ft.DataCell(ft.Text(f"R{round_number}"))]

        for player in PLAYERS:
            if is_out(player):
                round_entries.append(ft.DataCell(ft.Text("OUT", color=ft.Colors.RED_400)))
                continue

            val = input_fields[player].value.strip() if input_fields[player].value else ""
            score = int(val) if val.lstrip("-").isdigit() else 0

            scores[player].append(score)
            total = get_total(player)
            input_fields[player].value = ""

            if total >= TARGET_SCORE:
                score_cards[player]["total"].value = str(total)
                score_cards[player]["total"].color = ft.Colors.RED_400
                score_cards[player]["status"].value = "OUT"
                score_cards[player]["status"].color = ft.Colors.RED_400
                score_cards[player]["container"].bgcolor = ft.Colors.RED_900
                score_cards[player]["container"].border = ft.border.all(1, ft.Colors.RED_400)
                input_fields[player].disabled = True
                round_entries.append(ft.DataCell(ft.Text(f"{score} (OUT)", color=ft.Colors.RED_400)))
            else:
                score_cards[player]["total"].value = str(total)
                round_entries.append(ft.DataCell(ft.Text(str(score))))

        history_table.rows.insert(0, ft.DataRow(cells=round_entries))
        round_number += 1
        page.update()
        check_winner()

    def reset_game(e):
        nonlocal round_number
        round_number = 1
        history_table.rows.clear()
        for player in PLAYERS:
            scores[player] = []
            score_cards[player]["total"].value = "0"
            score_cards[player]["total"].color = ft.Colors.GREEN_ACCENT
            score_cards[player]["status"].value = "Active"
            score_cards[player]["status"].color = ft.Colors.GREEN_400
            score_cards[player]["container"].bgcolor = ft.Colors.SURFACE_CONTAINER_HIGHEST
            score_cards[player]["container"].border = None
            input_fields[player].disabled = False
            input_fields[player].value = ""
        page.update()

    btn_submit = ft.FilledButton("Submit Round", on_click=submit_round, expand=True)
    btn_reset = ft.OutlinedButton("Reset Game", on_click=reset_game, expand=True)

    page.add(
        ft.Column(
            [
                title,
                subtitle,
                cards_row,
                ft.Divider(height=10),
                ft.Text("Enter Round Scores", weight=ft.FontWeight.BOLD),
                inputs_row,
                ft.Row([btn_submit, btn_reset], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(height=10),
                ft.Text("History Log", weight=ft.FontWeight.BOLD),
                ft.Row([history_table], scroll=ft.ScrollMode.ADAPTIVE),
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=10,
        )
    )


if __name__ == "__main__":
    flet_app(target=main)