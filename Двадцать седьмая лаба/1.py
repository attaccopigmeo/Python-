"""Дано дерево поиска и корень дерева P1. Удалить в дереве вершину со значением
K. При замене содержимого удаляемой вершины использовать данные из ее левого поддерева.
После удаления вывести строку с описанием исходного дерева в следующем формате:
<дерево>::=((<левое поддерево>)<вершина>(<правое поддерево>)) | ((<левое
поддерево>)<вершина>) | (<вершина>(<правое поддерево>)) <вершина>::=<цифра><цифра> |
<цифра> <левое поддерево>::=<дерево> <правое поддерево>::=<дерево> Например,
"(((1)2((3)4))5(6(7)))"
. Пробелы в результирующей строке отсутствуют, ссылки на пустые
деревья никак не выводятся."""