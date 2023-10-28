from src.core.use_case import GetAllCategories

if __name__ == "__main__":
    use_case = GetAllCategories("https://icebergcharts.com/")

    use_case.run()
