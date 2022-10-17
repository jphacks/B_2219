import Header from "../components/header";
import Layout from "../components/layout";
import RepoForm from "../components/repo_form";

import styles from "../components/repo_form"

const TopPage = () => {
  return (
    <Layout>
      <Header />
      <RepoForm />
    </Layout>
  )
};

export default TopPage;
