import messages


WriteEventsCmd = '\x82'
WriteEventsCompletedCmd = '\x83'

#: Command code - message class mapping
classes = {
    WriteEventsCmd: messages.WriteEvents,
    WriteEventsCompletedCmd: messages.WriteEventsCompleted,
}
