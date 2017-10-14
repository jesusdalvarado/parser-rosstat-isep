# todo: create txt file in code, not in command line
def make_txt(source_file_pdf):
	pass

# todo: yield page 4 table contents
def yield_rows_from_txt(source_file_txt):
    yield 0
    yield ["Валовой внутренний продукт, млрд.рублей", 
           "41782,11)"]
    yield 0
    yield ["Продукция сельского хозяйства, млрд.рублей",
           "712,6", "104,7", "149,1", "101,5", "105,7",
           "138,3", "104,7"]
   
gen = yield_rows_from_xml(source_file_xml='oper.xml')


# skipping the top row with column names
_ = next(gen)

# skip second row, it has omissions  
row1 = next(gen)
assert row1[0] == "Валовой внутренний продукт, млрд.рублей"
assert row1[1] == "41782,11)"
    
# skip second row, it has omissions    
_ = next(gen) 

# check third row
row3 =  next(gen)
assert row3 == ["Продукция сельского хозяйства, млрд.рублей",
                "712,6", "104,7", "149,1", "101,5", "105,7",
                "138,3", "104,7"]

# not todo:
# convert values like "41782,11)" to  float(41782.1)
