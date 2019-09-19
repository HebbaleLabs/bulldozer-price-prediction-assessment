

def main():
    """
    This is the entrypoint for the testing phase.

    Some sample code is provided below, to demonstrate how to implement the Testing phase
    """
    #
    # # load or recreate the model based on training data
    # model = load_model()
    #
    # # Read the testing data
    # test_file_path = os.path.join(os.curdir, 'data/', 'Test.csv')
    # df_test = pd.read_csv(test_file_path, low_memory=False, parse_dates=["saledate"])
    #
    # Clean up testing data before supplying it to model for prediction
    # test_df = ...
    #
    # # apply the model on the testing data to make predictions
    # predicted_vals = make_predictions(model, test_df)
    #
    # # save the predictions in the submission file in the data/ directory
    # # For example, when using Pandas, ...
    #
    # submission = pd.DataFrame({'SalesID': test_df.SalesID, 'SalePrice': predicted_vals})
    # submission_file_path = os.path.join(os.curdir, 'data/', 'submission.csv')
    # submission.to_csv(submission_file_path, index=False)


if __name__ == "__main__":
    main()
