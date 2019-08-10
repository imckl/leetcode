# 以 Unix 风格给出一个文件的绝对路径，你需要简化它。或者换句话说，将其转换为规范路径。
#
# 在 Unix 风格的文件系统中，一个点（.）表示当前目录本身；此外，两个点 （..） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。更多信息请参阅：Linux / Unix中的绝对路径 vs 相对路径
#
# 请注意，返回的规范路径必须始终以斜杠 / 开头，并且两个目录名之间必须只有一个斜杠 /。最后一个目录名（如果存在）不能以 / 结尾。此外，规范路径必须是表示绝对路径的最短字符串。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/simplify-path
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution:

    def simplifyPath(self, path: str) -> str:

        # 如果无路径，直接返回
        if not path:
            return path

        stack = []

        # 构造路径数组，并排除数组内的空值
        path = [file for file in path.split('/') if file]

        # 遍历路径
        for file in path:
            # 文件名为'.'，不做任何处理
            if file == '.':
                continue
            # 文件名为'..'，栈顶值出栈
            elif file == '..':
                try:
                    stack.pop()
                # 如果栈为空，则不做任何处理
                except IndexError:
                    continue
            # 文件名确定，则将文件名置入栈顶
            else:
                stack.append(file)

        # 按照格式返回结果
        return '/' + '/'.join(stack)
