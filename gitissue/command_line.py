import pkg_resources

def main():
    version = pkg_resources.require("gitissue")[0].version
    print(f"git-issue version {version}")
