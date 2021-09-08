from datetime import datetime



class Test_Log:
    
    menudefs = [
                ('run', [
                         ('Test Log', '<<test_log>>'),
                         ] ),
                ]
        
    def __init__(self, editwin):
        "Initialize the settings for this extension."
        self.editwin = editwin
        self.text = editwin.text
        self.formatter = editwin.fregion
        self.text_frame = editwin.text_frame

    def test_log_event(self, event = None):
        now = datetime.now()
        self.text.tag_add('sel', '1.0', 'end')
        head, tail, chars, lines = self.formatter.get_region()
        self.text.tag_remove('sel', '1.0', 'end')
        current_time = now.strftime("%H:%M:%S")
        lines.append(current_time)
        f = open("/Users/anshul/Documents/test_logging.txt", "a")
        f.writelines(str(lines))
        f.writelines("\n")
        f.close()
        return "break"

    








        
