class UserMetrics:
    '''
        Customization data for get 
        from users to show as option 
        to could invest in the project.
    '''
    def __init__(self):
        # Use Methods instead of properties by security
        # to get the lasted and safest data
        pass
    
    def getUsers(self) -> int:
        '''
            How much registered users exist.
        '''
        userCounter: int = 1
        return userCounter

    def getActive(self) -> int:
        '''
            How Much users has chat or post
            this week.
        '''
        activesCounter: int = 1
        return activesCounter

    def getPosts(self) -> int:
        '''
            How Much Post in total
            has been maded.
        '''
        postCounter: int = 1
        return postCounter

    def getChats(self) -> int:
        '''
            How much message from all users
            has been sended.
        '''
        chatCounter:int = 1
        return chatCounter

    def getCosts(self) -> list[float, str]:
        '''
            Give 2-items list: price and currency.
        '''
        minimum: list[float, str] = [40.00, 'USD']
        # Make This Only for show as worrks the convertions
        minimum[0] = (minimum[0] * 1500)
        minimum[1] = 'ARS'
        # Give the converted value
        return minimum

    def getIncomes(self) -> list[float, int]:
        '''
            Similar logic to getCosts method but
            for give incomes from investments and
            users.
        '''
        incoming: list[float, str] = [0, 'ARS']
        return incoming

    def getGains(self) -> list[float, int]:
        '''
            Calculate gains that leave the
            project.
        '''
        return (self.getIncomes() - self.getCosts())