#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

form="""
<form method="post" >
	<p>What is your birthday? </p>
	<br>
	<lable> Month <input type="text" name='month' > </lable>
	<lable> Day <input type="text" name="day"> </lable>
	<lable> Year <input type="text" name="year" > </lable>
	<div style="color: red">%(error)s</div>
	<br>
	<br>
	<input type="submit" > 

</form>


"""

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

def valid_day(day):
    if day.isdigit()==True:
        day=int(day)
        if day >0 and day <= 31:
            return True
    return False

def valid_month(month):
    for i in months:
        if i.lower() == month.lower():
            return True
    return False

def valid_year(year):
    if year.isdigit():
        year = int(year)                       
        if year>=1900 and year<=2020:
            return True
    return False

#"Im part of the test"

class MainPage(webapp2.RequestHandler):

   def get(self):
   	self.response.out.write(form %{"error": "" })

#   		self.write_form()
#       	self.response.out.write(form%{"error":"Im part of the test"})
 
   def post(self):
   		user_month=valid_month(self.request.get('month') )
   		user_year=valid_year(self.request.get('year') )
   		user_day=valid_day(self.request.get('day') )
 	                       

   		if(user_day and user_year and user_month):
   			self.response.out.write("Thanks! That's a valid day!")                          
   		else:		
   			self.response.out.write(form%{"error":"This is something invalid,try again friend"})


app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)


