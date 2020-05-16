class Arguments:

  # gets the number of arguments when split by whitespace
  def argslen(args=None):
    if args is None:
      args = ""
    if len(args) == 0:
        return "0"
    splitargs = None
    if splitargs is None:
        splitargs = args.split()

    return str(splitargs)

    # gets the argument at the given index, split by whitespace
    def arg(splitargs=None, args=None):
        # Stubbed
        return ""
