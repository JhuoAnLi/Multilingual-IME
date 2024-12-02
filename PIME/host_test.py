    from multilingual_ime.muti_ime import KeyEventHandler
    import time
    import keyboard

    class HostPolyKey:
        def __init__(self):
            self.my_keyeventhandler = KeyEventHandler(verbose_mode=True)
            self.input_sentence = ""
            # self.avg_time, self.num_of_test = 0, 0
            # self.threshold = 0.3
            # self.last_keypress_time = 0
            # self.check = False
            # self.context = ""
            # self.start_time = time.time()
            # self.Token_Length = []
            # self.token_idx = 0
            # self.result1 = ""
            # self.result2 = ""
            # self.cursor_pos = 0
            # self.candidatelist = []
            # self.candidatelist_visible = True
        
        def run(self):
            while True:
                with open(r"C:\Users\super\Desktop\PolyKey\pimeinput.txt", "r", encoding="utf-8") as file:
                    keyinput = file.readline()
                    
                if keyinput == "": 
                    continue
                # but if the previous keyinput is the same as the current keyinput, might have this condition
                if keyinput != self.input_sentence:
                    output_string = ""
                    self.input_sentence = keyinput
                    self.my_keyeventhandler.handle_key(keyinput)
                    print(self.my_keyeventhandler.total_composition_words)
                    print("candidatelist: ", self.my_keyeventhandler.candidate_word_list)
                    for i in range(len(self.my_keyeventhandler.total_composition_words)):
                        output_string += self.my_keyeventhandler.total_composition_words[i]
                    print("output: ", output_string)
                    
                    with open (r"C:\Users\super\Desktop\PolyKey\pimeoutput.txt", "w", encoding="utf-8") as file:
                        file.write(output_string)
                    
                    self.my_keyeventhandler.slow_handle() 
                    
                    print(self.my_keyeventhandler.total_composition_words)
                    print("candidatelist: ", self.my_keyeventhandler.candidate_word_list)
                    for i in range(len(self.my_keyeventhandler.total_composition_words)):
                        output_string += self.my_keyeventhandler.total_composition_words[i]
                    print("output: ", output_string)
                    
                    with open (r"C:\Users\super\Desktop\PolyKey\pimeoutput.txt", "w", encoding="utf-8") as file:
                        file.write(output_string)
                    
                    
                        # file.write(",".join(candidate.word for candidate in self.my_keyeventhandler.candidate_word_list))
                    # print("--------------------")
                    # print("--------------------")
                    # # 好 B.txt another function compare previous B.txt with current B.txt, then update (another thread while true)
                    # print(self.my_keyeventhandler.total_composition_words)
                    # print("candidatelist: ", self.my_keyeventhandler.candidate_word_list)
                    # for i in range(len(self.my_keyeventhandler.total_composition_words)):
                    #     output_string += self.my_keyeventhandler.total_composition_words[i]
                    # print(output_string)
                    
                    # with open(r"C:\Users\super\Desktop\PolyKey\pimeoutput.txt", "w", encoding="utf-8") as file:
                    #     file.write(output_string + "\n")
                    #     file.write(",".join(candidate for candidate in self.my_keyeventhandler.candidate_word_list))
                    #     # file.write(str(self.my_keyeventhandler.composition_index()) + "\n")
                    #     # file.write(str(self.my_keyeventhandler.in_selection_mode()) + "\n")
                    #     # file.write(str(self.my_keyeventhandler.selection_index()))
        
        # def run(self):  
        #     while True:
        #         # lines = "284ru8 cl3"
        #         with open(r"C:\Users\super\Desktop\PolyKey\pimeinput.txt", "r", encoding="utf-8") as file:
        #             lines = file.readlines()
                    
        #         if len(lines) == 0:
        #             continue
                
        #         keycheck = ""
        #         if len(lines) > 1:
        #             keycheck = lines[-1].strip()            
                
        #         if lines[0].strip().replace("\x00", "") != self.input_sentence :
        #             self.input_sentence = lines[0].strip().replace("\x00", "")
        #             self.num_of_test += 1
        #             self.start_time = time.time()
        #             self.result1 = self.my_IMEHandler.get_candidate_sentences(self.input_sentence, self.context)
        #             for i in range(len(self.result1[0]["sentence"])):
        #                 self.Token_Length.append(len(self.result1[0]["sentence"][i]))
        #             self.token_idx = len(self.result1[0]["sentence"])
        #             self.result2 = self.my_IMEHandler.get_best_sentence(self.input_sentence, self.context)
        #             self.cursor_pos = len(self.result2) + self.Token_Length[-1]
        #             end_time = time.time()
        #             self.avg_time = (self.avg_time * (self.num_of_test - 1) + end_time - self.start_time) / self.num_of_test
        #             print(f"Inference time: {time.time() - self.start_time}, avg time: {self.avg_time}")
        #             print(self.result1)
        #             print(self.result2) 
        #             self.candidatelist = self.my_IMEHandler.get_token_candidates(self.result1[0]["sentence"][self.token_idx-1])
        #             print(self.candidatelist)
        #             with open(r"C:\Users\super\Desktop\PolyKey\pimeoutput.txt", "w", encoding="utf-8") as file:
        #                 file.write(self.result2+'\n')
        #                 file.write(str(len(self.result2))+'\n')
        #                 file.write(",".join(candidate.word for candidate in self.candidatelist))
        #         # LEFT
        #         if keycheck == "l":
        #             print("LEFT")
        #             with open(r"C:\Users\super\Desktop\PolyKey\pimeinput.txt", "w", encoding="utf-8") as file:
        #                 file.write(self.input_sentence)
        #             if self.token_idx == 0:
        #                 continue
        #             if self.check == True:
        #                 self.check = False
        #                 self.cursor_pos = len(self.result2[:self.token_idx-1]) + self.Token_Length[self.token_idx-1]+1
        #             CursorMove_temp_str=self.Left_cursordetect()
        #             print("CursorMove_temp_str: ", CursorMove_temp_str)
        #             print("Cursor Position: ", self.cursor_pos)
        #             time.sleep(0.3)
        #             with open(r"C:\Users\super\Desktop\PolyKey\pimeoutput.txt", "w", encoding="utf-8") as file:
        #                 file.write(CursorMove_temp_str+'\n')
        #                 file.write(str(self.cursor_pos)+'\n')
        #                 if self.candidatelist_visible and self.token_idx != 0:
        #                     file.write(",".join(candidate.word for candidate in self.candidatelist))
                
        #         # RIGHT
        #         if keycheck == "r":
        #             print("RIGHT")
        #             with open(r"C:\Users\super\Desktop\PolyKey\pimeinput.txt", "w", encoding="utf-8") as file:
        #                 file.write(self.input_sentence)
        #             if self.token_idx == len(self.result1[0]["sentence"]):
        #                 continue
        #             CursorMove_temp_str=self.Right_cursordetect()
        #             print("CursorMove_temp_str: ", CursorMove_temp_str)
        #             print("Cursor Position: ", self.cursor_pos)
        #             time.sleep(0.3)
        #             with open(r"C:\Users\super\Desktop\PolyKey\pimeoutput.txt", "w", encoding="utf-8") as file:
        #                 file.write(CursorMove_temp_str+'\n')
        #                 file.write(str(self.cursor_pos)+'\n')
        #                 if self.candidatelist_visible:
        #                     file.write(",".join(candidate.word for candidate in self.candidatelist))   
        
        # def Left_cursordetect(self):
        #     if self.Token_Length[self.token_idx-1] != 0:
        #         self.candidatelist_visible = False
        #         temp_str = self.result2[:self.token_idx-1] + "".join(self.result1[0]["sentence"][self.token_idx-1 : self.token_idx])+self.result2[self.token_idx:]
        #         self.Token_Length[self.token_idx-1] -= 1
        #         self.cursor_pos -= 1
        #     else:
        #         self.check = True
        #         self.candidatelist_visible = True
        #         self.token_idx -= 1
        #         if self.token_idx != 0:
        #             self.candidatelist = self.my_IMEHandler.get_token_candidates(self.result1[0]["sentence"][self.token_idx-1])
        #         self.cursor_pos = len(self.result2[:self.token_idx])
        #         temp_str = self.result2
        #     return temp_str
        
        # def Right_cursordetect(self):
        #     if self.Token_Length[self.token_idx] != len(self.result1[0]["sentence"][self.token_idx])-1:
        #         self.candidatelist_visible = False
        #         temp_str = self.result2[:self.token_idx] + "".join(self.result1[0]["sentence"][self.token_idx : self.token_idx+1])+self.result2[self.token_idx+1:]        
        #         self.Token_Length[self.token_idx] += 1
        #         self.cursor_pos += 1
        #     else:
        #         self.token_idx += 1
        #         self.candidatelist_visible = True
        #         self.candidatelist = self.my_IMEHandler.get_token_candidates(self.result1[0]["sentence"][self.token_idx-1])
        #         self.cursor_pos = len(self.result2[:self.token_idx])
        #         temp_str = self.result2
        #     return temp_str      
            
            
    if __name__ == "__main__":
        HostPolyKey().run()
