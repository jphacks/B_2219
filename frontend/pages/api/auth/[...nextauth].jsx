import NextAuth from "next-auth"
import GithubProvider from "next-auth/providers/github"

const authOptions = {
  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_ID,
      clientSecret: process.env.GITHUB_SECRET,
    }),
  ],
  callbacks: {
    jwt: async ({ token, user, account, profile, isNewUser }) => {
      if (account?.access_token) {
        token.access_token = account.access_token;
      }
      return token;
    },
    session: async ({ session, token, user }) => {
      if (session?.user) {
        session.user.id = token.sub;
        session.access_token = token.access_token;
      }
      return session;
    },
  },
  secret: process.env.NEXTAUTH_SECRET,
};

export default NextAuth(authOptions);
export { authOptions };
