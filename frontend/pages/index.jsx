import { useSession } from "next-auth/react";

import Header from "../components/header";
import Layout from "../components/layout";
import RepoForm from "../components/repo_form";

import styles from "../components/top.module.css"

const TopPage = () => {
  const { data: session } = useSession();
  if (!session) {
    return (
      <Layout className={styles.not_logged_in}>
        <Header />
        <main className={styles.not_logged_in}>
          <p>SyaKyo!は先人のリポジトリを写経して学べるプログラミング学習サイトです！</p>
        </main>
      </Layout>
    );
  }
 
  return (
    <Layout className={styles.logged_in}>
      <Header />
      <main className={styles.logged_in}>
        <RepoForm />
      </main>
    </Layout>
  )
};

export default TopPage;
