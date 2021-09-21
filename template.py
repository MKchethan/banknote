import os

dirs = [
    os.path.join("data", "raw"),                       #inside data we have raw
    os.path.join("data", "processed"),                 #inside data we have processed[datasplit]
    "notebooks",                                       #if we want to use like jupiter notebooks like that
    "saved_models",                                    #here where we save our models
    "src"                                              #to keep our dataset
]
for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)
    with open(os.path.join(dir_, ".gitkeep"), "w") as f:
        pass


files = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src", "__init__.py")
]
for file_ in files:
    with open(file_, "w") as f:
        pass



