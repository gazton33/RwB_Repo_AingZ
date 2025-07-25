import os


def create_scaffold(base_dir, project_names, create_repo=True):
    # Directorios y archivos generales
    structure = [
        'knowledge/knowledge_demo.md',
        'config/config_demo.json',
        'config/.env.example',
        'onboarding/checklist_coverage.md',
        'onboarding/template_demo.md',
        'docs/croquis_demo.md',
        'docs/imagen_demo.png',
        'docs/README.md',
        'README.md',
        'changelog.md',
        'master_plan_aingz_infrastructure.md',
        '.gitignore',
    ]

    # Scaffold para cada proyecto
    project_structure = [
        'README.md',
        'matrices/matriz_demo.md',
        'workflows/workflow_demo.md',
        'scripts/script_demo.py',
        'scripts/README.md',
        'logs/logs_demo.log',
        'backups/backup_demo.zip',
        'notebooks/notebook_demo.ipynb',
        'docs/croquis_demo.md',
        'docs/README.md',
    ]

    if create_repo:
        # Crear carpetas/archivos generales
        for path in structure:
            full_path = os.path.join(base_dir, path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            if not os.path.exists(full_path):
                with open(full_path, 'w') as f:
                    f.write(f'# Placeholder for {os.path.basename(full_path)}\n')

    # Crear carpetas/archivos de proyectos
    projects_dir = os.path.join(base_dir, 'projects')
    for project in project_names:
        for path in project_structure:
            full_path = os.path.join(projects_dir, project, path)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            if not os.path.exists(full_path):
                with open(full_path, 'w') as f:
                    f.write(f'# Placeholder for {os.path.basename(full_path)} in {project}\n')


def menu():
    print("\n=== RAW GOLD Multi-Proyecto Scaffold ===")
    print("1. Crear un nuevo repo RAW GOLD desde cero")
    print("2. Agregar proyecto(s) a un repo RAW GOLD existente")
    opcion = input("Selecciona una opción (1 o 2): ").strip()
    while opcion not in ("1", "2"):
        opcion = input("Opción inválida. Selecciona 1 o 2: ").strip()
    return opcion


def select_repo():
    bases = [d for d in os.listdir('.') if os.path.isdir(d) and os.path.exists(os.path.join(d, 'projects'))]
    if not bases:
        print("No se encontraron repos RAW GOLD existentes en el directorio actual.")
        return None
    print("Repositorios detectados:")
    for i, d in enumerate(bases):
        print(f"{i+1}. {d}")
    sel = input("Selecciona el número del repo destino: ").strip()
    while not sel.isdigit() or not (1 <= int(sel) <= len(bases)):
        sel = input("Número inválido. Intenta de nuevo: ").strip()
    return bases[int(sel)-1]


def input_projects():
    print("Escribe el/los nombres de proyecto(s) separados por coma:")
    names = input("Proyectos: ").strip()
    projects = [n.strip() for n in names.split(",") if n.strip()]
    return projects


if __name__ == "__main__":
    opcion = menu()
    if opcion == "1":
        base_directory = input("Nombre para el nuevo repo RAW GOLD: ").strip()
        projects = input_projects()
        create_scaffold(base_directory, projects, create_repo=True)
        print(f"Repo '{base_directory}' y proyectos creados correctamente.")
    else:
        repo = select_repo()
        if repo:
            projects = input_projects()
            create_scaffold(repo, projects, create_repo=False)
            print(f"Proyectos agregados a repo existente: {repo}")
        else:
            print("No se realizó ninguna acción.")
