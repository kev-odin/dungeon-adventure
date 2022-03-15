from app.model.dungeon.dungeon_builder import DungeonBuilder
from app.controller.game_controller import GameController
from app.view.dungeon_adventure_GUI import dungeon_adventure_GUI

if __name__ == "__main__":
    db = DungeonBuilder()
    gv = dungeon_adventure_GUI()
    gc = GameController(db, gv)
    gc.frame_setup()
