"""
Build static HTML site from directory of HTML templates and plain files.

Andrew DeOrio <awdeorio@umich.edu>
"""
from os.path import abspath, dirname, join, isdir, expanduser, commonprefix, relpath, basename, normpath, splitext
from os import walk, makedirs
import sys
from shutil import copyfile, move
import json
from jinja2 import Environment, FileSystemLoader
from jinja2.exceptions import TemplateError
import click

APPNAME_PATH_PLACEHOLDER = "APPNAME" # reflected in the dirnames in <proj_root>/templates
PROJECT_ROOT_DIR = dirname(dirname(abspath(__file__)))
TEMPLATE_DIR = join(PROJECT_ROOT_DIR, 'templates')

def get_subpaths(root):
    dirpaths, filepaths = [], []
    for dirpath, _, filenames in walk(root):
        if dirpath != root:
            dirpaths.append(dirpath)
        for filename in filenames:
            filepath = join(dirpath, filename)
            filepaths.append(filepath)

    # make paths relative to root
    common_prefix = root
    dirpaths = [relpath(path, common_prefix) for path in dirpaths]
    filepaths = [relpath(path, common_prefix) for path in filepaths]

    return dirpaths, filepaths

def replace_appname_in_paths(root, appname):
    paths_to_change = []
    for dirpath, _, _ in walk(root):
        last_dir = basename(normpath(dirpath))
        if APPNAME_PATH_PLACEHOLDER in last_dir:
            paths_to_change.append(dirpath)
    
    for path_to_change in paths_to_change:
        changed_path = path_to_change
        while APPNAME_PATH_PLACEHOLDER in changed_path:
            changed_path = changed_path.replace(APPNAME_PATH_PLACEHOLDER, appname)
        
        move(path_to_change, changed_path)

def prepare_dir_structure(target_dir, sub_dirs):
    for sub_dir in sub_dirs:
        full_target_path = join(target_dir, sub_dir)
        makedirs(full_target_path)

def copy_and_render_files(source_dir, target_dir, rel_filepaths, context):
    env = Environment(loader=FileSystemLoader('templates'))
    for rel_filepath in rel_filepaths:
        stripped_rel_filename, ext = splitext(rel_filepath)

        if ext == ".temp":
            # templated file, need to render
            abs_target_path = join(target_dir, stripped_rel_filename)
            try:
                template = env.get_template(rel_filepath)
                rendered_content = template.render(**context, go=abs_target_path)
            except TemplateError as err:
                print("Error_Jinja: jinja2 template", rel_filepath)
                print("{}: {}".format(type(err).__name__, err))
                sys.exit(1)

            # Write output file
            with open(abs_target_path, "w") as output_file:
                output_file.write(rendered_content)
        else:
            # just copy over
            abs_source_path = join(source_dir, rel_filepath)
            abs_target_path = join(target_dir, rel_filepath)
            copyfile(abs_source_path, abs_target_path)

@click.command()
@click.argument("output_dir")
@click.argument("appname")
def main(output_dir, appname):
    """Templated static website generator."""
    home_dir = expanduser("~")
    output_dir = join(home_dir, output_dir)
    if not isdir(output_dir):
        makedirs(output_dir)
    else:
        print("Path {} already exists. Exiting", output_dir)
        sys.exit(1)

    context = {"appname" : appname}

    template_rel_dirpaths, template_rel_filepaths = get_subpaths(TEMPLATE_DIR)

    prepare_dir_structure(output_dir, template_rel_dirpaths)
    copy_and_render_files(TEMPLATE_DIR, output_dir, template_rel_filepaths, context)
    replace_appname_in_paths(output_dir, appname)


    """
        # Input (template) and output (rendered html) filenames
        output_filename = os.path.join(dirname, "index.html")

        # Render template
        try:
            template = template_env.get_template(template_filename)
            output_content = template.render(**context, go=output_filename)
        except jinja2.exceptions.TemplateError as err:
            print("Error_Jinja: jinja2 template", template_filename)
            print("{}: {}".format(type(err).__name__, err))
            sys.exit(1)

        # Write output file
        with open(output_filename, "w") as output_file:
            output_file.write(output_content)
    """

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()

