from http.client import responses

from playwright.sync_api import Playwright
orderPayload ={"orders":
                   [
                       {
                        "country": "Austria'",
                        "productOrderedId": "6960eac0c941646b7a8b3e68"
                       }
                   ]
                }
token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTg2ZmU0NmM5NDE2NDZiN2FkYmIxMDQiLCJ1c2VyRW1haWwiOiJoaXRlc2hzaGlAZ21haWwuY29tIiwidXNlck1vYmlsZSI6ODIwODE5NDk5OSwidXNlclJvbGUiOiJjdXN0b21lciIsImlhdCI6MTc3MDQ1ODg5MywiZXhwIjoxODAyMDE2NDkzfQ.xeSycwFp0O8x4p3HQCAQvTccZqQgL9Vd9ksyvgX1FiU"

class ApiUtils:

    def createOrder(self,playwright:Playwright):
        # request.newContext() creates a context for API
        tokenFromApi = self.generateToken(playwright)
        request = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response =request.post("api/ecom/order/create-order",
                     data=orderPayload,
                     headers={"Content-Type": "application/json",
                              "Authorization":token}
                     )
        print(response.json())
        return response.json()


    def generateToken(self,playwright:Playwright):
        requests = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        response=requests.post("api/ecom/auth/login",
                      data={"userEmail":"hiteshshi@gmail.com",
                            "userPassword":"LearnApi@123",
                            },
                      )
        assert response.ok
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def getOrder(self,playwright:Playwright):
        tokenFromApi=self.generateToken(playwright)
        requests = playwright.request.new_context(base_url="https://rahulshettyacademy.com/")
        requests = requests.post("api/ecom/order/get-orders-details",
                                 data ={"id":"69874633dc40b48f12c4c59b"},
                                headers = {"Content-Type": "application/json",
                                            "Authorization": token}
                                 )