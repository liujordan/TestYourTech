class Click(ActionBase):
	def _execute(self):
		try:
            element = WebDriverWait(browser1, 10).until(
                EC.presence_of_element_located((By.XPATH, selector1))
            )
            element.click()
            return True
        except:
            print("timedout", function, selector1, value1)
            return False