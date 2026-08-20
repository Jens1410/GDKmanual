import pathlib

def define_env(env):

    # Beispiel: dynamische Variable
    env.variables['copyright'] = "© 2026 Jens"

    # Beispiel: Filter für Farben
    def farbe(typ):
        mapping = {
            "primär": env.variables.get("farbe_primär", "#009485"),
            "warnung": env.variables.get("farbe_warnung", "#ff4444"),
        }
        return mapping.get(typ, "#000000")

    env.filters["farbe"] = farbe

    # Makro zum Einbinden externer Dateien (HTML, Markdown, Text)
    @env.macro
    def include_file(path):
        # Pfad relativ zum docs-Verzeichnis
        full_path = pathlib.Path(env.project_dir) / env.conf['docs_dir'] / path
        return full_path.read_text(encoding="utf-8")
