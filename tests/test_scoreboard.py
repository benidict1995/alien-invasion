import json
import pygame
import pytest

from stats import scoreboard as scoreboard_module
from stats.scoreboard import Scoreboard


class DummySettings:
    def __init__(self):
        self.bg_color = (255, 255, 255)


class DummyStats:
    def __init__(self, score=0, high_score=0, ship_life=3):
        self.score = score
        self.high_score = high_score
        self.ship_life = ship_life


class DummyAI:
    def __init__(self, screen, settings, stats):
        self.screen = screen
        self.settings = settings
        self.stats = stats


def setup_pygame():
    # Initialize pygame modules needed for fonts and surfaces
    pygame.init()


def teardown_pygame():
    pygame.quit()


def test_scoreboard_initialization(tmp_path, monkeypatch):
    """Scoreboard initializes images and ship sprites without touching repo files."""
    setup_pygame()

    # Make scoreboard use a temporary file path under tmp_path
    monkeypatch.setattr(scoreboard_module, "Path", lambda p: tmp_path.joinpath(p))

    # Replace Ship with a lightweight fake to avoid image loads
    class FakeShip(pygame.sprite.Sprite):
        def __init__(self, ai_game):
            super().__init__()
            self.rect = pygame.Rect(0, 0, 40, 20)

    monkeypatch.setattr(scoreboard_module, "Ship", FakeShip)

    screen = pygame.Surface((800, 600))
    settings = DummySettings()
    stats = DummyStats(score=123, high_score=0, ship_life=3)
    ai = DummyAI(screen, settings, stats)

    sb = Scoreboard(ai)

    assert hasattr(sb, "score_image")
    assert hasattr(sb, "high_score_image")
    assert hasattr(sb, "ships")
    assert len(sb.ships) != stats.ship_life

    teardown_pygame()


def test_save_and_load_high_score(tmp_path, monkeypatch):
    """Saving writes JSON and loading restores the high score."""
    setup_pygame()

    monkeypatch.setattr(scoreboard_module, "Path", lambda p: tmp_path.joinpath(p))

    class FakeShip(pygame.sprite.Sprite):
        def __init__(self, ai_game):
            super().__init__()
            self.rect = pygame.Rect(0, 0, 40, 20)

    monkeypatch.setattr(scoreboard_module, "Ship", FakeShip)

    screen = pygame.Surface((400, 300))
    settings = DummySettings()
    stats = DummyStats(score=0, high_score=42, ship_life=1)
    ai = DummyAI(screen, settings, stats)

    sb = Scoreboard(ai)
    # Set the desired high score after Scoreboard init (load_high_score may have reset it)
    stats.high_score = 42
    # save to the tmp path
    sb.save_high_score()

    saved_path = tmp_path.joinpath("file/high_score.json")
    assert saved_path.exists()
    contents = saved_path.read_text()
    assert json.loads(contents) == 42

    # Reset and load
    stats.high_score = 0
    sb.load_high_score()
    assert stats.high_score == 42

    teardown_pygame()


def test_check_high_score_updates(tmp_path, monkeypatch):
    """check_high_score updates high score when current score exceeds it."""
    setup_pygame()

    monkeypatch.setattr(scoreboard_module, "Path", lambda p: tmp_path.joinpath(p))

    class FakeShip(pygame.sprite.Sprite):
        def __init__(self, ai_game):
            super().__init__()
            self.rect = pygame.Rect(0, 0, 40, 20)

    monkeypatch.setattr(scoreboard_module, "Ship", FakeShip)

    screen = pygame.Surface((200, 200))
    settings = DummySettings()
    stats = DummyStats(score=150, high_score=100, ship_life=2)
    ai = DummyAI(screen, settings, stats)

    sb = Scoreboard(ai)
    # update
    sb.check_high_score()
    assert stats.high_score == 150

    teardown_pygame()
