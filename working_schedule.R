# 排班表计算函数
"""
  What do we try to solve?
    We need a working schedule for the editer desk in which everyone
    works a whole day and rest a whole day under the condition that 
    the daily editing work must be finished and one editor and one ratifier
    are present at the desk.
    Note that:
    We need one editor and one ratifier to finish one day's work. That is the 
    condition we must meet.

input: 
  editor = c(editor1,editor2,...) a vector of editor's names
  ratifier = c(r1, r2, ...), a vector of ratifier's names
  p = float,  a parameter equals the proportion of editor's labor to ratifier's labor
  i.e. p = (total labor of editors)/(total labor of ratifers)

output:
    a csv file storing a working schedule for both editors and ratifers in 
  one compete period of t weeks
  
  primitive structure:

    let one complete period be t weeks
    let each ratifer's labor be x days in one t
    let each editor's labor be x*p

    such that 

      length(ratifier) * x + length(editor) * x * p = 2 * 7 * t,

    which means that the total labor of ratifiers and the total labor of editors 
      equal the amount of labor needed in one complete period t.
    
    firstly, we need find minimun x and minimun t such that t%x == 0 and x*p is an integer. is.integer()

    secondly, after find the x and the t, we can build the working schedule table.
      - This table can be a data frame whose column names are weekday names, rownames are index of weeks like 
      'Week One', 'Week Two', etc. 
      - The first column is a factor vector which has only two levels, namely 'editor' and 'ratifier'.
          Notes: in the table, 'editor' and 'ratifier', each of them will appear in every other row,
                    or say each week must have one row for 'editor' and one row for 'ratifier'.
      - The next seven columns are weekday columns whose values are names of editors and ratifiers.
          Example: if a row has a factor value of 'editor', then each names in this row will
                    do the editor job in this specific week.

    thirdly, write the schedule table into a csv file and output it.

    done!

"""