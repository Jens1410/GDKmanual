def define_env(env):
    # Zugriff auf YAML-Variablen ist automatisch vorhanden
    # env.variables['projekt'] etc.

    # Beispiel: dynamische Variable
    env.variables['copyright'] = "© 2026 Jens"

    # Beispiel: Filter für Farben
    def farbe(typ):
        mapping = {
            "primär": env.variables["farbe_primär"],
            "warnung": env.variables["farbe_warnung"],
        }
        return mapping.get(typ, "#000000")

    env.filters["farbe"] = farbe
