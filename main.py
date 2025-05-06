from pathlib import Path

def define_env(env):
    @env.macro
    def include(file_name):
        includes_dir = Path(__file__).parent / "_includes"
        with open(includes_dir / file_name, "r", encoding="utf-8") as f:
            return f.read()

    @env.macro
    def include_equations(prefix, start, end):
        includes_dir = Path(__file__).parent / "_includes"
        result = ""
        for i in range(start, end + 1):
            file_name = f"{prefix}_{i}.md"
            file_path = includes_dir / file_name
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    result += f.read() + "\n\n"
        return result
