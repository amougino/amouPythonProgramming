from PIL import Image
from graph import Graph


def find_adjacent(board, vert_pos):
    adj = []
    x, y = vert_pos
    len_x, len_y = len(board[y]), len(board)
    if x < len_x-1 and board[y][x+1] in "+SE":
        adj.append((x+1, y))

    if y < len_y-1 and board[y+1][x] in "+SE":
        adj.append((x, y+1))

    if x != 0 and board[y][x-1] in "+SE":
        adj.append((x-1, y))

    if y != 0 and board[y-1][x] in "+SE":
        adj.append((x, y-1))
    return adj


def create_graph(board):
    vert_count = len("".join(("".join(x) for x in board)))
    graph = Graph(vert_count)
    for y, row in enumerate(board):
        for x, item in enumerate(row):
            id = x + y * len(row)

            if item in "+SE":
                for i, j in find_adjacent(board, (x, y)):
                    id_adj = i + j * len(row)
                    graph.add_uedge(id, id_adj)
    return graph


def create_board(image_path):
    img = Image.open(image_path)
    width, height = img.size
    board = []
    extreme = ["E", "S"]
    for y in range(height):
        row = []
        for x in range(width):
            value = "+" if img.getpixel((x, y)) == (255,255,255) else "-"
            # This will never happen more than twice
            #if (x == 0 or y == 0 or x == width - 1 or y == height - 1) and value == "+":
            #    value = extreme[-1]
            #    extreme.pop()
            row.append(value)
        board.append(row)
    board[0][0] = "S"
    board[558][398] = "E"
    return board


def create_solution(board, path):
    height = len(board)
    width = len(board[0])

    img = Image.new("RGB", (width, height))
    for y, row in enumerate(board):
        for x, item in enumerate(row):
            value_dict = {"+": (255, 255, 255),
                          "-": (0, 0, 0),
                          "S": (0, 150, 0),
                          "E": (150, 0, 0),
                          }
            value = value_dict[item]
            if (x, y) in path and not (item in "SE"):

                delta = int((255 / len(path)) * path.index((x,y)))
                value = (0 + delta, 0, 255 - delta)
            img.putpixel((x, y), value)
    img.save("200_280_b_solution.png")

board = create_board("/Users/amou/Desktop/Python/currentProjects/200_280_b_labyrinth.png")

graph = create_graph(board)

start_pos = "".join(("".join(x) for x in board)).find("S")
end_pos = "".join(("".join(x) for x in board)).find("E")


path = graph.bfs(start_pos, end_pos)
path_coord = []
for vert_id in path:
    row_length = len(board[0])
    x, y = vert_id % row_length, vert_id // row_length
    path_coord.append((x, y))

create_solution(board, path_coord)