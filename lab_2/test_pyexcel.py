import pyexcel

list_id =[
    {
        "Name": "Adam",
        "Age": 28
    },
    
    {
        "Name": "Beatrice",
        "Age": 26
    },

    {
        "Name": "Dean",
        "Age": 27
    }
]

pyexcel.save_as(records= list_id , dest_file_name="your_file.xlsx")