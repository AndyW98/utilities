import sys

def progressbar(it, prefix="", size=60, file=sys.stdout, progress_char='#'):
    """
    Display a progress bar

    @param  it             The list being iterated over
    @param  prefix         Prefix of the progress bar
    @param  size           Size of the displayed progress bar
    @param  file           The output stream
    @param  progress_char  The character showing progress done
    """
    count = len(it)

    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" %
            (prefix, progress_char*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()