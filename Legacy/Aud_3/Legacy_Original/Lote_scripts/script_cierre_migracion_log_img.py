# Script de cierre y migración de LOG e IMG para RwB
# Requiere: Python 3.7+, permisos de escritura en el repo
# Ajustado para ejecutarse en 'C:/AingZ/AingZ_RwB' (Windows)

import os
import shutil

# Ruta base del repo en tu PC
REPO_BASE = r'C:/AingZ/AingZ_RwB'
LEGACY_DIR = os.path.join(REPO_BASE, 'Legacy')
BACKUP_DIR = os.path.join(REPO_BASE, 'backup', 'logs')

IMG_LIST = [
    os.path.join(REPO_BASE, 'Legacy/purgatorio/PR/DataAIEng/DOC/RwB_PR_DataAIEng_DOC_v1d1_WIP_ChatGPT_Image_13_jul_2025,_22_35_55.png'),
    os.path.join(REPO_BASE, 'Legacy/purgatorio/PR/DataAIEng/DOC/RwB_PR_DataAIEng_DOC_v1d1_WIP_ChatGPT_Image_14_jul_2025,_10_08_00.png')
]
LOG_LIST = [
    os.path.join(REPO_BASE, 'Legacy/PR/projects/Misc/logs/logs_demo.log'),
    os.path.join(REPO_BASE, 'Legacy/PR/projects/FoodProj/logs/logs_demo.log'),
    os.path.join(REPO_BASE, 'Legacy/PR/projects/DataAIEng/logs/logs_demo.log'),
    os.path.join(REPO_BASE, 'Legacy/PR/projects/ResInv/logs/logs_demo.log'),
    os.path.join(REPO_BASE, 'Legacy/PR/projects/AudioPrj/logs/logs_demo.log'),
    os.path.join(REPO_BASE, 'Legacy/PR/projects/ResInn/logs/logs_demo.log'),
    os.path.join(REPO_BASE, 'Legacy/migration_errors.txt'),
    os.path.join(REPO_BASE, 'Legacy/purgatorio/PR/DataAIEng/LOG/RwB_PR_DataAIEng_LOG_v1d1_WIP_main.main'),
    os.path.join(REPO_BASE, 'Legacy/purgatorio/PR/DataAIEng/LOG/RwB_PR_DataAIEng_LOG_v1d1_WIP_main_dup1.main'),
    os.path.join(REPO_BASE, 'Legacy/purgatorio/PR/DataAIEng/LOG/RwB_PR_DataAIEng_LOG_v1d1_WIP_HEAD.HEAD'),
    os.path.join(REPO_BASE, 'Legacy/purgatorio/PR/DataAIEng/LOG/RwB_PR_DataAIEng_LOG_v1d1_WIP_HEAD_dup1.HEAD')
]

def move_logs():
    os.makedirs(BACKUP_DIR, exist_ok=True)
    for log_path in LOG_LIST:
        if os.path.isfile(log_path):
            file_name = os.path.basename(log_path)
            backup_name = file_name.replace('.log', f'_legacy.log').replace('.main', f'_legacy.main').replace('.HEAD', f'_legacy.HEAD').replace('.txt', '_legacy.txt')
            dest_path = os.path.join(BACKUP_DIR, backup_name)
            shutil.move(log_path, dest_path)
            print(f"[LOG MIGRADO] {log_path} -> {dest_path}")
        else:
            print(f"[NO ENCONTRADO] {log_path}")

def remove_imgs():
    for img_path in IMG_LIST:
        if os.path.isfile(img_path):
            os.remove(img_path)
            print(f"[IMG ELIMINADA] {img_path}")
        else:
            print(f"[IMG NO ENCONTRADA] {img_path}")

def main():
    print("=== Migración de LOG e IMG (cierre de ciclo) ===")
    move_logs()
    remove_imgs()
    print("\n---\nRecuerda actualizar manualmente registro_trazabilidad_total.md, changelog.md y checklist_incongruencias.md para finalizar el cierre.")

if __name__ == "__main__":
    main()
