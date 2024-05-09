class Delete:
    '''
    passes in variables that contain .pack() or .place()
    and deletes them
    '''
    def delete_widget(self,
                      *variables):
        for variable in variables:
            variable.pack_forget()
            variable.place_forget()
    
    '''
    passes in a list to delete them
    '''
    def delete_bundle(self,
                      variable_list):
        for variable in variable_list:
            variable.pack_forget()
            variable.place_forget()