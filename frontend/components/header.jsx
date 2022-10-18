import Link from "next/link";

import styles from "./header.module.css";
import LoginButton from "../components/login-button";

const Header = () => {
  return (
    <div className={styles.header_container}>
      <header>
        <Link href="/">ShaKyo!</Link>
        <LoginButton />
      </header>
    </div>
  );
};

export default Header;
