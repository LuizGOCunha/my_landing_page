from dataclasses import dataclass


@dataclass
class ProjectInfo:
    """Holds project info to be used in html parsing, will probably become a db model in the future."""

    name: str
    link: str
    description: str


def gather_engineer_description() -> list[str]:
    """Gathers the description into a list of paragraphs to be formatted into html."""
    with open("general_info/eng_description.txt", "r") as description_file:
        description = description_file.read()
        return description.split("\n")


def gather_engineer_projects() -> list[dict]:
    """Gather projects information from the appropriate source."""

    @dataclass
    class ProjectInfo:
        name: str
        link: str
        description: str

    with open("general_info/eng_projects.csv", "r") as project_file:
        projects_lines = project_file.read().split("\n")
        projects_info = []
        for projects_line in projects_lines:
            if projects_line:
                info_cells = projects_line.split(",")
                projects_info.append(ProjectInfo(name=info_cells[0], link=info_cells[1], description=info_cells[2]))
        return projects_info
