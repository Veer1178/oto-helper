"""

This function is used to convert the passed video file into a audio file for further processing. 

"""

"""We use *args and **kwargs as an argument when we have no doubt about the number of arguments we should pass in a function"""
def extract_audio(video_file_name, audio_output_file=audio.mp3, *args, **kwargs):

    """

    #TODO
    
    - Fill this with the documentation of the code. i.e. the docstring.
    - Accomadate for the different video file types such as mp4, mkv, raw, etc. 

    - Add arguments, if needed

    - Add requirements to requirements.txt usign "pip freeze > requirements.txt"

    - Let the user have option to choose different audio formats such as .wav, .mp3, etc



    """
    video_file_extensions = (".mp4", ".mkv", ".raw", ".mov", ".flv", ".wmv", ".avi", ".webm")
    if video_file_name.endswith((video_file_extensions)):
        
        '''
        
        #code
        
        '''
        
    else:
        print("Video file format not supported")
