from pathlib import Path

from streamlit.testing.v1 import AppTest

from logic_utils import check_guess


APP_PATH = Path(__file__).resolve().parents[1] / "app.py"

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == ("Win", "🎉 Correct!")

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == ("Too High", "📉 Go LOWER!")

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == ("Too Low", "📈 Go HIGHER!")

#FIX: Added regression test to ensure hints are not reversed, which was a prior bug
def test_regression_hints_are_not_reversed():
    # Regression test for the prior bug where guidance was flipped.
    high_outcome, high_message = check_guess(60, 50)
    low_outcome, low_message = check_guess(40, 50)

    assert high_outcome == "Too High"
    assert high_message == "📉 Go LOWER!"
    assert low_outcome == "Too Low"
    assert low_message == "📈 Go HIGHER!"


def test_new_game_resets_history_and_attempts_for_selected_difficulty(monkeypatch):
    generated_secrets = iter([42, 77])
    monkeypatch.setattr("random.randint", lambda low, high: next(generated_secrets))

    app = AppTest.from_file(str(APP_PATH))
    app.run()

    app.selectbox[0].set_value("Hard").run()
    app.session_state["history"] = [12, 34]
    app.session_state["attempts"] = 1
    app.session_state["status"] = "lost"

    app.button[1].click().run()

    assert app.session_state["history"] == []
    assert app.session_state["attempts"] == 5
    assert app.session_state["status"] == "playing"
    assert 1 <= app.session_state["secret"] <= 100
