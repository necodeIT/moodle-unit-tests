from typing import List
import git
import os
from moodle import MOODLE_PATH

REPO_URL: str = 'https://github.com/moodle/moodle'

def get_repo() -> git.Repo:
    if os.path.exists(MOODLE_PATH):
        return git.Repo(MOODLE_PATH)
    else:
        return git.Repo.clone_from(REPO_URL, MOODLE_PATH)
        

def install_moodle(version: str) -> None:
    get_repo().git.execute(['git', 'checkout', version])
    pass

def get_moodle_version() -> str:
    return get_repo().active_branch.name

def get_moodle_versions() -> List[str]:
    """
    Returns a list of available moodle versions to install.
    """
    
  
    return [tag.name for tag in get_repo().tags][-1::-1]
    