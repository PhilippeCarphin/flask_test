from app.sgfparser import make_tree_from_file_path
from app.sgfwriter import write_sgf_file

def turn_file(file_path, output_file_path):
    mt = make_tree_from_file_path(file_path)
    mt.rotate()
    write_sgf_file(mt, output_file_path)
